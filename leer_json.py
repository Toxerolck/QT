import leer_json
from PyQt6 import QtCore, QtGui, QtWidgets
import sys
#tienes que escribir la ruta global del archivo JSON para que lo muestre
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

        # Conecta la señal clicked del botón a la función que se encarga de leer y mostrar el archivo JSON
        self.boton.clicked.connect(self.mostrar_archivo_json)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Que Archivo. JSON quieres leer?"))
        self.boton.setText(_translate("MainWindow", "OK"))

    def mostrar_archivo_json(self):
        # Obtiene la ruta del archivo desde el QTextEdit "ruta"
        ruta_archivo = self.ruta.toPlainText()
        try:
            with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
                contenido = json.loads(archivo.read())  # Carga el contenido del archivo JSON en un diccionario
                # Convierte el diccionario de nuevo a una cadena de texto y lo muestra en el QTextEdit "mostrar", con 4 de sangria
                self.mostrar.setPlainText(json.dumps(contenido, indent=4))
        except FileNotFoundError:
            self.mostrar.setPlainText("Archivo no encontrado")
        except json.JSONDecodeError:
            self.mostrar.setPlainText("El archivo no es un archivo JSON válido")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
