from PyQt6 import QtCore, QtGui, QtWidgets
import serial
import time
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_temp = QtWidgets.QLabel(self.centralwidget)
        self.label_temp.setGeometry(QtCore.QRect(50, 50, 100, 20))
        self.label_temp.setObjectName("label_temp")
        self.label_hum = QtWidgets.QLabel(self.centralwidget)
        self.label_hum.setGeometry(QtCore.QRect(50, 100, 100, 20))
        self.label_hum.setObjectName("label_hum")
        self.label_temp_val = QtWidgets.QLabel(self.centralwidget)
        self.label_temp_val.setGeometry(QtCore.QRect(160, 50, 100, 20))
        self.label_temp_val.setObjectName("label_temp_val")
        self.label_hum_val = QtWidgets.QLabel(self.centralwidget)
        self.label_hum_val.setGeometry(QtCore.QRect(160, 100, 100, 20))
        self.label_hum_val.setObjectName("label_hum_val")
        self.pushButton_refresh = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_refresh.setGeometry(QtCore.QRect(50, 150, 100, 30))
        self.pushButton_refresh.setObjectName("pushButton_refresh")
        self.pushButton_exit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_exit.setGeometry(QtCore.QRect(200, 150, 100, 30))
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.lineEdit_com = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_com.setGeometry(QtCore.QRect(50, 200, 100, 30))
        self.lineEdit_com.setObjectName("lineEdit_com")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Conectar la señal clicked del botón de refrescar a la función actualizar_datos
        self.pushButton_refresh.clicked.connect(self.actualizar_datos)

        # Conectar la señal clicked del botón de salida a la función salir
        self.pushButton_exit.clicked.connect(QtWidgets.QApplication.instance().quit)

        # Configurar el temporizador para que llame a la función actualizar_datos cada 5 segundos
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.actualizar_datos)
        self.timer.start(500)  # 500 milisegundos = 0,5 segundos

        # Inicializar la conexión serial con el puerto COM ingresado por el usuario
        self.serial = 0

    # Función para traducir la interfaz gráfica
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DHT11 Sensor Data"))
        self.label_temp.setText(_translate("MainWindow", "Temperatura:"))
        self.label_hum.setText(_translate("MainWindow", "Humedad:"))
        self.pushButton_refresh.setText(_translate("MainWindow", "Actualizar"))
        self.pushButton_exit.setText(_translate("MainWindow", "Salir"))

    # Función para actualizar los datos de temperatura y humedad
    def actualizar_datos(self):
        # Obtener el puerto COM ingresado por el usuario
        puerto_com = self.lineEdit_com.text().strip()
        # Si no se ha establecido una conexión serial y se ha ingresado un puerto COM
        if not self.serial and puerto_com:
            try:
                # Intentar inicializar la conexión serial con el puerto COM especificado
                self.serial = serial.Serial(puerto_com, 9600, timeout=1)
            except serial.SerialException as e:
                # Imprimir un mensaje de error si no se puede abrir el puerto COM
                print("Error al abrir el puerto COM:", e)
        # Si hay una conexión serial establecida
        if self.serial:
            try:
                # Enviar comando al Arduino para solicitar los datos del sensor
                self.serial.write(b'r')
                # Leer la respuesta del Arduino
                data = self.serial.readline().decode().strip()
                # Dividir los datos en temperatura y humedad, lo divide por cada ","
                temperatura, humedad = data.split(',')
                # Actualizar las etiquetas con los nuevos valores de temperatura y humedad
                self.label_temp_val.setText(temperatura)
                self.label_hum_val.setText(humedad)
            except Exception as e:
                # Imprimir un mensaje de error si hay un error durante la comunicación serial
                print("Error durante la comunicación serial:", e)
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())

