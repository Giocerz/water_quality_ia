# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'OriginSelectListACpNdQ.ui'
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
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.backBtn = QPushButton(self.centralwidget)
        self.backBtn.setObjectName(u"backBtn")
        self.backBtn.setGeometry(QRect(5, 5, 41, 41))
        self.backBtn.setStyleSheet(u"border-radius: 20px;\n"
"border: 1px solid #00007f;\n"
"background-color: white;\n"
"color: #00007f;")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(-1, -1, 481, 281))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.originList = QListView(self.page)
        self.originList.setObjectName(u"originList")
        self.originList.setGeometry(QRect(60, 61, 351, 191))
        self.originList.setStyleSheet(u"border: 1px solid black;\n"
"border-radius: 10px;")
        self.originList.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.originList.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.verticalSlider = QSlider(self.page)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setGeometry(QRect(420, 60, 41, 191))
        self.verticalSlider.setStyleSheet(u"QSlider::groove:vertical{ \n"
"	background-color: rgb(234, 234, 234);\n"
"	height: 191px;\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QSlider::handle:vertical { \n"
"	background-color: #00007f;\n"
"    height: 60;\n"
"    width: 20px;\n"
"    line-height: 10px; \n"
"	margin-top: 0px; \n"
"	margin-bottom: 0px;\n"
"	border-radius: 20px; \n"
"}\n"
"\n"
"QSlider{\n"
"	background-color: rgb(234, 234, 234);\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"")
        self.verticalSlider.setPageStep(1)
        self.verticalSlider.setValue(0)
        self.verticalSlider.setOrientation(Qt.Vertical)
        self.verticalSlider.setInvertedAppearance(True)
        self.verticalSlider.setInvertedControls(False)
        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(140, 20, 221, 20))
        self.label.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.widgetKeyboard = QWidget(self.page_2)
        self.widgetKeyboard.setObjectName(u"widgetKeyboard")
        self.widgetKeyboard.setGeometry(QRect(0, 140, 480, 135))
        self.widgetKeyboard.setStyleSheet(u"background-color: rgb(234, 234, 234);")
        self.inputOrigin = QLineEdit(self.page_2)
        self.inputOrigin.setObjectName(u"inputOrigin")
        self.inputOrigin.setGeometry(QRect(120, 50, 251, 26))
        self.inputOrigin.setStyleSheet(u"border-color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 6px;\n"
"background-color: rgb(234, 234, 234);\n"
"font-size: 14px;")
        self.inputOrigin.setMaxLength(50)
        self.label_2 = QLabel(self.page_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(120, 20, 201, 21))
        self.confirmBtn = QPushButton(self.page_2)
        self.confirmBtn.setObjectName(u"confirmBtn")
        self.confirmBtn.setGeometry(QRect(170, 100, 111, 31))
        self.confirmBtn.setStyleSheet(u"border-radius: 20px;\n"
"background-color: #00007f;\n"
"color: white;\n"
"border: none;\n"
"border-radius: 15px;\n"
"font-size: 14px;")
        self.stackedWidget.addWidget(self.page_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.stackedWidget.raise_()
        self.backBtn.raise_()

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.backBtn.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Seleccione una opci\u00f3n", None))
        self.inputOrigin.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Otro origen...", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Escriba el origen", None))
        self.confirmBtn.setText(QCoreApplication.translate("MainWindow", u"Confirmar", None))
    # retranslateUi

