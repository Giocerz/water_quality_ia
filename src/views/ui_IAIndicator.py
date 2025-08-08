# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'IAIndicatorZVTCnZ.ui'
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
        Form.resize(240, 70)
        Form.setStyleSheet(u"QLabel {\n"
"	font-family: Poppins;\n"
"	font-size: 16px;\n"
"}\n"
"\n"
"QWidget {\n"
"	background-color: white;\n"
"}")
        self.nameLbl = QLabel(Form)
        self.nameLbl.setObjectName(u"nameLbl")
        self.nameLbl.setGeometry(QRect(10, 5, 201, 21))
        self.probLbl = QLabel(Form)
        self.probLbl.setObjectName(u"probLbl")
        self.probLbl.setGeometry(QRect(20, 30, 211, 31))
        self.probLbl.setStyleSheet(u"font-weight: bold;\n"
"background-color: transparent;")
        self.colorLbl = QLabel(Form)
        self.colorLbl.setObjectName(u"colorLbl")
        self.colorLbl.setGeometry(QRect(0, 0, 241, 71))
        self.colorLbl.setStyleSheet(u"border: 4px solid red;")
        self.colorLbl.raise_()
        self.nameLbl.raise_()
        self.probLbl.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.nameLbl.setText(QCoreApplication.translate("Form", u"\u00bfEs agua contaminada?", None))
        self.probLbl.setText(QCoreApplication.translate("Form", u"---", None))
        self.colorLbl.setText("")
    # retranslateUi

