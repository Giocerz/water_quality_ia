# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainMenuDyzSzc.ui'
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
"font-size:20px;\n"
"font-weight: 500;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QPushButton {\n"
"	height: 50px;\n"
"	border-radius: 25px;\n"
"	border: 1px solid #00007f;\n"
"	background-color: white;\n"
"	color: #00007f;\n"
"}")
        self.powerBtn = QPushButton(self.centralwidget)
        self.powerBtn.setObjectName(u"powerBtn")
        self.powerBtn.setGeometry(QRect(420, 209, 50, 50))
        self.powerBtn.setStyleSheet(u"")
        self.wifiBtn = QPushButton(self.centralwidget)
        self.wifiBtn.setObjectName(u"wifiBtn")
        self.wifiBtn.setGeometry(QRect(420, 144, 50, 50))
        self.wifiBtn.setStyleSheet(u"")
        self.updateBtn = QPushButton(self.centralwidget)
        self.updateBtn.setObjectName(u"updateBtn")
        self.updateBtn.setGeometry(QRect(420, 79, 50, 50))
        self.updateBtn.setStyleSheet(u"")
        self.helpBtn = QPushButton(self.centralwidget)
        self.helpBtn.setObjectName(u"helpBtn")
        self.helpBtn.setGeometry(QRect(420, 14, 50, 50))
        self.helpBtn.setStyleSheet(u"")
        self.monitoringBtn = QPushButton(self.centralwidget)
        self.monitoringBtn.setObjectName(u"monitoringBtn")
        self.monitoringBtn.setGeometry(QRect(10, 10, 195, 121))
        self.monitoringBtn.setStyleSheet(u"")
        self.calibrationBtn = QPushButton(self.centralwidget)
        self.calibrationBtn.setObjectName(u"calibrationBtn")
        self.calibrationBtn.setGeometry(QRect(215, 10, 195, 121))
        self.calibrationBtn.setStyleSheet(u"")
        self.bluetoothBtn = QPushButton(self.centralwidget)
        self.bluetoothBtn.setObjectName(u"bluetoothBtn")
        self.bluetoothBtn.setGeometry(QRect(215, 141, 195, 121))
        self.bluetoothBtn.setStyleSheet(u"")
        self.dataBtn = QPushButton(self.centralwidget)
        self.dataBtn.setObjectName(u"dataBtn")
        self.dataBtn.setGeometry(QRect(10, 141, 195, 121))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.powerBtn.setText("")
        self.wifiBtn.setText("")
        self.updateBtn.setText("")
        self.helpBtn.setText("")
        self.monitoringBtn.setText(QCoreApplication.translate("MainWindow", u"Monitoreo", None))
        self.calibrationBtn.setText(QCoreApplication.translate("MainWindow", u"Calibraci\u00f3n", None))
        self.bluetoothBtn.setText(QCoreApplication.translate("MainWindow", u"Bluetooth", None))
        self.dataBtn.setText(QCoreApplication.translate("MainWindow", u"Datos", None))
    # retranslateUi

