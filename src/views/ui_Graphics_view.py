# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Graphics_viewJfFVwx.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(480, 272)
        MainWindow.setStyleSheet(u"background-color: white;\n"
"font-family: Poppins;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QPushButton {\n"
"	height: 40px;\n"
"	border-radius: 20px;\n"
"	border: 1px solid #00007f;\n"
"	background-color: white;\n"
"	color: #00007f;\n"
"}\n"
"\n"
"QLabel {\n"
"	color: #00007f;\n"
"}\n"
"")
        self.graphWidget = QWidget(self.centralwidget)
        self.graphWidget.setObjectName(u"graphWidget")
        self.graphWidget.setGeometry(QRect(0, 61, 480, 171))
        self.backBtn = QPushButton(self.centralwidget)
        self.backBtn.setObjectName(u"backBtn")
        self.backBtn.setGeometry(QRect(5, 5, 41, 41))
        self.backBtn.setStyleSheet(u"")
        self.sampleLbl = QLabel(self.centralwidget)
        self.sampleLbl.setObjectName(u"sampleLbl")
        self.sampleLbl.setGeometry(QRect(10, 230, 181, 16))
        self.sampleLbl.setStyleSheet(u"font-size: 16px;")
        self.valueLbl = QLabel(self.centralwidget)
        self.valueLbl.setObjectName(u"valueLbl")
        self.valueLbl.setGeometry(QRect(10, 250, 181, 16))
        self.valueLbl.setStyleSheet(u"font-size: 16px;")
        self.titleLbl = QLabel(self.centralwidget)
        self.titleLbl.setObjectName(u"titleLbl")
        self.titleLbl.setGeometry(QRect(270, 20, 201, 20))
        self.titleLbl.setStyleSheet(u"font-size: 16px;\n"
"font-weight: bold;")
        self.titleLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.prevPageBtn = QPushButton(self.centralwidget)
        self.prevPageBtn.setObjectName(u"prevPageBtn")
        self.prevPageBtn.setGeometry(QRect(55, 5, 41, 41))
        self.prevPageBtn.setStyleSheet(u"")
        self.nextPageBtn = QPushButton(self.centralwidget)
        self.nextPageBtn.setObjectName(u"nextPageBtn")
        self.nextPageBtn.setGeometry(QRect(105, 5, 41, 41))
        self.nextPageBtn.setStyleSheet(u"")
        self.dateLbl = QLabel(self.centralwidget)
        self.dateLbl.setObjectName(u"dateLbl")
        self.dateLbl.setGeometry(QRect(200, 230, 271, 16))
        self.dateLbl.setStyleSheet(u"font-size: 16px;")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.backBtn.setText("")
        self.sampleLbl.setText(QCoreApplication.translate("MainWindow", u"Muestra:", None))
        self.valueLbl.setText(QCoreApplication.translate("MainWindow", u"Valor:", None))
        self.titleLbl.setText(QCoreApplication.translate("MainWindow", u"Solidos Totales Disueltos", None))
        self.prevPageBtn.setText("")
        self.nextPageBtn.setText("")
        self.dateLbl.setText(QCoreApplication.translate("MainWindow", u"Fecha:", None))
    # retranslateUi

