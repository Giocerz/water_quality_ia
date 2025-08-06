# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Bluetooth_ConnectedLzCUVg.ui'
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
"font-family: Poppins;\n"
"font-size:18px;\n"
"font-weight: 500;")
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
        self.backBtn = QPushButton(self.centralwidget)
        self.backBtn.setObjectName(u"backBtn")
        self.backBtn.setGeometry(QRect(10, 10, 41, 41))
        self.backBtn.setStyleSheet(u"")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 200, 481, 61))
        self.label.setStyleSheet(u"font-size: 24px;")
        self.label.setAlignment(Qt.AlignCenter)
        self.imageLbl = QLabel(self.centralwidget)
        self.imageLbl.setObjectName(u"imageLbl")
        self.imageLbl.setGeometry(QRect(0, 10, 481, 191))
        MainWindow.setCentralWidget(self.centralwidget)
        self.imageLbl.raise_()
        self.backBtn.raise_()
        self.label.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.backBtn.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"CitizenAP0003", None))
        self.imageLbl.setText("")
    # retranslateUi

