# Importar las bibliotecas necesarias
from PyQt6 import QtCore, QtGui, QtWidgets
import csv

#La ruta del archivo tiene que ser global.
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 640)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 341, 16))
        self.label.setObjectName("label")
        self.ruta = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.ruta.setGeometry(QtCore.QRect(10, 40, 391, 31))
        self.ruta.setObjectName("ruta")
        self.mostrar = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.mostrar.setGeometry(QtCore.QRect(10, 80, 411, 431))
        self.mostrar.setObjectName("mostrar")
        self.boton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.boton.setGeometry(QtCore.QRect(20, 540, 121, 41))
        self.boton.setObjectName("boton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Conectar la señal clicked del botón a la función mostrar_archivo_csv
        self.boton.clicked.connect(self.mostrar_archivo_csv)

    # Método para traducir la interfaz gráfica
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Qué archivo CSV quieres leer?"))
        self.boton.setText(_translate("MainWindow", "OK"))
    def mostrar_archivo_csv(self):
        # Obtener la ruta del archivo desde el QTextEdit "ruta"
        ruta_archivo = self.ruta.toPlainText()
        try:
            # Abrir el archivo CSV en modo lectura
            with open(ruta_archivo, 'r', newline='', encoding='utf-8') as archivo:
                # Leer el contenido del archivo CSV utilizando csv.reader
                contenido = csv.reader(archivo)
                # Convertir el contenido en una cadena de texto y mostrarlo en el QTextEdit "mostrar"
                texto_mostrar = ""
                for fila in contenido:
                    texto_mostrar += ', '.join(fila) + '\n'
                self.mostrar.setPlainText(texto_mostrar)
        except FileNotFoundError:
            # Manejar la excepción si el archivo no se encuentra
            self.mostrar.setPlainText("Archivo no encontrado")
        except Exception as e:
            # Manejar otras excepciones y mostrar el mensaje de error
            self.mostrar.setPlainText(f"Error: {str(e)}")
if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
