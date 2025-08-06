# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UpdateViewecCrPQ.ui'
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
"font: 18px Poppins;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.backBtn = QPushButton(self.centralwidget)
        self.backBtn.setObjectName(u"backBtn")
        self.backBtn.setGeometry(QRect(5, 10, 41, 41))
        self.backBtn.setStyleSheet(u"height: 40px;\n"
"border-radius: 20px;\n"
"border: 1px solid #00007f;\n"
"background-color: white;\n"
"color: #00007f;\n"
"font-weight: 500;\n"
"font-size: 11px;")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(110, 10, 261, 51))
        self.label.setStyleSheet(u"color: #00007f;")
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(152, 80, 151, 51))
        self.label_2.setStyleSheet(u"font-weight: bold;\n"
"color: #00007f;\n"
"font-size: 24px;")
        self.infoLbl = QLabel(self.centralwidget)
        self.infoLbl.setObjectName(u"infoLbl")
        self.infoLbl.setGeometry(QRect(60, 150, 361, 51))
        self.infoLbl.setAlignment(Qt.AlignCenter)
        self.updateBtn = QPushButton(self.centralwidget)
        self.updateBtn.setObjectName(u"updateBtn")
        self.updateBtn.setGeometry(QRect(155, 210, 171, 41))
        self.updateBtn.setStyleSheet(u"height: 40px;\n"
"border-radius: 20px;\n"
"border: 1px solid #00007f;\n"
"background-color: white;\n"
"color: #00007f;\n"
"font-weight: 500;\n"
"font-size: 16px;")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(282, 80, 50, 50))
        self.label_3.setStyleSheet(u"background-color: #00007f;\n"
"border-radius: 25px;")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(295, 92, 31, 31))
        self.label_4.setStyleSheet(u"font-weight: bold;\n"
"color: white;\n"
"font-size: 24px;\n"
"background-color: transparent;")
        self.infoVersion = QLabel(self.centralwidget)
        self.infoVersion.setObjectName(u"infoVersion")
        self.infoVersion.setGeometry(QRect(152, 120, 131, 21))
        self.infoVersion.setStyleSheet(u"font-size: 14px;")
        self.infoVersion.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.backBtn.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Actualizaciones del sistema", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Citizen AP", None))
        self.infoLbl.setText(QCoreApplication.translate("MainWindow", u"No hay actualizaciones disponibles", None))
        self.updateBtn.setText(QCoreApplication.translate("MainWindow", u"Actualizar", None))
        self.label_3.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"UI", None))
        self.infoVersion.setText(QCoreApplication.translate("MainWindow", u"Versi\u00f3n 1.0.0", None))
    # retranslateUi

