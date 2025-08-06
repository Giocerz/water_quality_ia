# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SelectItRainedPopupWheeSa.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(480, 272)
        Form.setStyleSheet(u"font: 14px Poppins;")
        self.lblOpacity = QLabel(Form)
        self.lblOpacity.setObjectName(u"lblOpacity")
        self.lblOpacity.setGeometry(QRect(0, 0, 480, 320))
        self.lblOpacity.setStyleSheet(u"background-color: black;")
        self.Widget1 = QWidget(Form)
        self.Widget1.setObjectName(u"Widget1")
        self.Widget1.setEnabled(True)
        self.Widget1.setGeometry(QRect(104, 20, 271, 221))
        self.Widget1.setStyleSheet(u"border-radius: 20px;\n"
"background-color: white;")
        self.confirmBtn = QPushButton(self.Widget1)
        self.confirmBtn.setObjectName(u"confirmBtn")
        self.confirmBtn.setGeometry(QRect(85, 170, 101, 41))
        self.confirmBtn.setStyleSheet(u"QPushButton {\n"
"	border: 1px solid #00007f;\n"
"	background-color: white;\n"
"	color: #00007f;\n"
"	font-size: 14px;\n"
"	font-family: Poppins;\n"
"	font-weight: 500;\n"
"}")
        self.yesCheckBox = QCheckBox(self.Widget1)
        self.yesCheckBox.setObjectName(u"yesCheckBox")
        self.yesCheckBox.setGeometry(QRect(70, 50, 91, 31))
        self.yesCheckBox.setStyleSheet(u"QCheckBox {\n"
"	background-color: transparent;\n"
"	height: 10px;\n"
"	font: 14px \"Poppins\";\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Ancho del indicador */\n"
"    height: 20px; /* Alto del indicador */\n"
"    border-radius: 4px; /* Bordes redondeados */\n"
"    border: 2px solid #666; /* Borde del indicador */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color: #00007f; /* Color de fondo cuando est\u00e1 marcado */\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    background-color: transparent;\n"
"}")
        self.label = QLabel(self.Widget1)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 20, 171, 16))
        self.label.setAlignment(Qt.AlignCenter)
        self.noCheckBox = QCheckBox(self.Widget1)
        self.noCheckBox.setObjectName(u"noCheckBox")
        self.noCheckBox.setGeometry(QRect(70, 90, 91, 31))
        self.noCheckBox.setStyleSheet(u"QCheckBox {\n"
"	background-color: transparent;\n"
"	height: 10px;\n"
"	font: 14px \"Poppins\";\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Ancho del indicador */\n"
"    height: 20px; /* Alto del indicador */\n"
"    border-radius: 4px; /* Bordes redondeados */\n"
"    border: 2px solid #666; /* Borde del indicador */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color: #00007f; /* Color de fondo cuando est\u00e1 marcado */\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    background-color: transparent;\n"
"}")
        self.idkCheckBox = QCheckBox(self.Widget1)
        self.idkCheckBox.setObjectName(u"idkCheckBox")
        self.idkCheckBox.setGeometry(QRect(70, 130, 91, 31))
        self.idkCheckBox.setStyleSheet(u"QCheckBox {\n"
"	background-color: transparent;\n"
"	height: 10px;\n"
"	font: 14px \"Poppins\";\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Ancho del indicador */\n"
"    height: 20px; /* Alto del indicador */\n"
"    border-radius: 4px; /* Bordes redondeados */\n"
"    border: 2px solid #666; /* Borde del indicador */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color: #00007f; /* Color de fondo cuando est\u00e1 marcado */\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    background-color: transparent;\n"
"}")
        self.yesCheckBox.raise_()
        self.confirmBtn.raise_()
        self.label.raise_()
        self.noCheckBox.raise_()
        self.idkCheckBox.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lblOpacity.setText("")
        self.confirmBtn.setText(QCoreApplication.translate("Form", u"Confirmar", None))
        self.yesCheckBox.setText(QCoreApplication.translate("Form", u"S\u00ed", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u00bfLlovi\u00f3 recientemente?", None))
        self.noCheckBox.setText(QCoreApplication.translate("Form", u"No", None))
        self.idkCheckBox.setText(QCoreApplication.translate("Form", u"No lo s\u00e9", None))
    # retranslateUi

