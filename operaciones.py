# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Interfaz.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(299, 249)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 39, 71, 21))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(20, 170, 61, 21))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 180, 61, 21))
        self.pushButton_2.setObjectName("pushButton_2")
        self.Ingresar = QtWidgets.QTextEdit(Dialog)
        self.Ingresar.setGeometry(QtCore.QRect(20, 70, 131, 16))
        self.Ingresar.setObjectName("Ingresar")
        self.Ingresar_2 = QtWidgets.QTextEdit(Dialog)
        self.Ingresar_2.setGeometry(QtCore.QRect(170, 70, 121, 16))
        self.Ingresar_2.setObjectName("Ingresar_2")
        self.Resultado2 = QtWidgets.QLabel(Dialog)
        self.Resultado2.setGeometry(QtCore.QRect(150, 40, 61, 20))
        self.Resultado2.setText("")
        self.Resultado2.setObjectName("Resultado2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        #Presionar
        self.pushButton.clicked.connect(self.sumar)
        self.pushButton_2.clicked.connect(self.restar)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Resultado:"))
        self.pushButton.setText(_translate("Dialog", "Sumar"))
        self.pushButton_2.setText(_translate("Dialog", "Restar"))
        self.Ingresar.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Ingrese el primer numero</p></body></html>"))
        self.Ingresar_2.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Ingrese el segundo numero</p></body></html>"))

    def sumar(self):
        num1 = float(self.Ingresar.toPlainText())
        num2 = float(self.Ingresar_2.toPlainText())
        resultado = num1 + num2
        self.Resultado2.setText(str(resultado))

    def restar(self):
        num1 = float(self.Ingresar.toPlainText())
        num2 = float(self.Ingresar_2.toPlainText())
        resultado = num1 - num2
        self.Resultado2.setText(str(resultado))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())