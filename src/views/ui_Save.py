# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SaveAxbshv.ui'
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
"font: 14px Poppins;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.backBtn = QPushButton(self.centralwidget)
        self.backBtn.setObjectName(u"backBtn")
        self.backBtn.setGeometry(QRect(5, 5, 41, 41))
        self.backBtn.setStyleSheet(u"height: 40px;\n"
"border-radius: 20px;\n"
"border: 1px solid #00007f;\n"
"background-color: white;\n"
"color: #00007f;\n"
"font-weight: 500;\n"
"font-size: 11px;")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 0, 481, 271))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.inputPlace = QLineEdit(self.page)
        self.inputPlace.setObjectName(u"inputPlace")
        self.inputPlace.setGeometry(QRect(90, 30, 251, 26))
        self.inputPlace.setStyleSheet(u"border-color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 6px;\n"
"background-color: rgb(234, 234, 234);")
        self.inputPlace.setMaxLength(50)
        self.widgetKeyboard = QWidget(self.page)
        self.widgetKeyboard.setObjectName(u"widgetKeyboard")
        self.widgetKeyboard.setGeometry(QRect(0, 140, 480, 135))
        self.widgetKeyboard.setStyleSheet(u"background-color: rgb(234, 234, 234);")
        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(90, 8, 161, 21))
        self.nextBtn = QPushButton(self.page)
        self.nextBtn.setObjectName(u"nextBtn")
        self.nextBtn.setGeometry(QRect(350, 90, 111, 31))
        self.nextBtn.setStyleSheet(u"border-radius: 20px;\n"
"background-color: #00007f;\n"
"color: white;\n"
"border: none;\n"
"border-radius: 15px;")
        self.itRainedBtn = QPushButton(self.page)
        self.itRainedBtn.setObjectName(u"itRainedBtn")
        self.itRainedBtn.setGeometry(QRect(90, 90, 251, 31))
        self.itRainedBtn.setStyleSheet(u"border-radius: 20px;\n"
"border: 2px solid grey;\n"
"border-radius: 6px;")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.prevBtn = QPushButton(self.page_2)
        self.prevBtn.setObjectName(u"prevBtn")
        self.prevBtn.setGeometry(QRect(30, 230, 111, 31))
        self.prevBtn.setStyleSheet(u"border-radius: 20px;\n"
"background-color: #00007f;\n"
"color: white;\n"
"border: none;\n"
"border-radius: 15px;\n"
"")
        self.gpsBtn = QPushButton(self.page_2)
        self.gpsBtn.setObjectName(u"gpsBtn")
        self.gpsBtn.setGeometry(QRect(55, 100, 180, 31))
        self.gpsBtn.setStyleSheet(u"border-radius: 20px;\n"
"background-color: #00007f;\n"
"color: white;\n"
"border: none;\n"
"border-radius: 15px;\n"
"\n"
"")
        self.label_4 = QLabel(self.page_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(100, 70, 281, 21))
        self.saveBtn = QPushButton(self.page_2)
        self.saveBtn.setObjectName(u"saveBtn")
        self.saveBtn.setGeometry(QRect(339, 230, 111, 31))
        self.saveBtn.setStyleSheet(u"border-radius: 20px;\n"
"background-color: #00007f;\n"
"color: white;\n"
"border: none;\n"
"border-radius: 15px;\n"
"\n"
"")
        self.selectFolderBtn = QPushButton(self.page_2)
        self.selectFolderBtn.setObjectName(u"selectFolderBtn")
        self.selectFolderBtn.setGeometry(QRect(150, 180, 181, 31))
        self.selectFolderBtn.setStyleSheet(u"border-radius: 20px;\n"
"color: #00007f;\n"
"border: 2px solid #00007f;\n"
"border-radius: 15px;\n"
"\n"
"")
        self.folderLbl = QLabel(self.page_2)
        self.folderLbl.setObjectName(u"folderLbl")
        self.folderLbl.setGeometry(QRect(100, 150, 281, 21))
        self.label_2 = QLabel(self.page_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(120, 10, 221, 16))
        self.setManualLocationBtn = QPushButton(self.page_2)
        self.setManualLocationBtn.setObjectName(u"setManualLocationBtn")
        self.setManualLocationBtn.setGeometry(QRect(245, 100, 180, 31))
        self.setManualLocationBtn.setStyleSheet(u"border-radius: 20px;\n"
"color: #00007f;\n"
"border: 2px solid #00007f;\n"
"border-radius: 15px;\n"
"\n"
"")
        self.originBtn = QPushButton(self.page_2)
        self.originBtn.setObjectName(u"originBtn")
        self.originBtn.setGeometry(QRect(119, 30, 241, 31))
        self.originBtn.setStyleSheet(u"border-radius: 20px;\n"
"border: 1px solid black;\n"
"border-radius: 5px;")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.openCreateFolderBtn = QPushButton(self.page_3)
        self.openCreateFolderBtn.setObjectName(u"openCreateFolderBtn")
        self.openCreateFolderBtn.setGeometry(QRect(135, 230, 211, 31))
        self.openCreateFolderBtn.setStyleSheet(u"border-radius: 20px;\n"
"background-color: #00007f;\n"
"color: white;\n"
"border: none;\n"
"border-radius: 15px;\n"
"")
        self.scrollArea = QScrollArea(self.page_3)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(50, 0, 431, 231))
        self.scrollArea.setStyleSheet(u"border: opx;")
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 431, 231))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalSlider = QSlider(self.page_3)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setGeometry(QRect(10, 50, 31, 181))
        self.verticalSlider.setLayoutDirection(Qt.LeftToRight)
        self.verticalSlider.setStyleSheet(u"QSlider::groove:vertical{ \n"
"    background-color: rgb(234, 234, 234);\n"
"    width: 30px;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QSlider::handle:vertical { \n"
"    background-color: #00007f;\n"
"   	width: 20px;\n"
"	height: 50px;\n"
"	margin-top: 0px; \n"
"	margin-bottom: 0px;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QSlider{\n"
"    background-color: rgb(234, 234, 234);\n"
"    border-radius: 10px;\n"
"}\n"
"")
        self.verticalSlider.setMinimum(0)
        self.verticalSlider.setMaximum(99)
        self.verticalSlider.setPageStep(2)
        self.verticalSlider.setValue(0)
        self.verticalSlider.setSliderPosition(0)
        self.verticalSlider.setTracking(True)
        self.verticalSlider.setOrientation(Qt.Vertical)
        self.verticalSlider.setInvertedAppearance(True)
        self.verticalSlider.setInvertedControls(True)
        self.emptyFoldersNoticeLbl = QLabel(self.page_3)
        self.emptyFoldersNoticeLbl.setObjectName(u"emptyFoldersNoticeLbl")
        self.emptyFoldersNoticeLbl.setGeometry(QRect(90, 30, 351, 81))
        self.emptyFoldersNoticeLbl.setStyleSheet(u"color: grey;\n"
"font-size: 24px;")
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.label_7 = QLabel(self.page_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(120, 38, 61, 21))
        self.folderName = QLineEdit(self.page_4)
        self.folderName.setObjectName(u"folderName")
        self.folderName.setGeometry(QRect(120, 60, 241, 26))
        self.folderName.setStyleSheet(u"border-color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 6px;\n"
"font: 14px \"Poppins\";\n"
"background-color: rgb(234, 234, 234);")
        self.folderName.setMaxLength(50)
        self.label_8 = QLabel(self.page_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(190, 10, 111, 21))
        self.label_8.setStyleSheet(u"")
        self.widgetKeyboard2 = QWidget(self.page_4)
        self.widgetKeyboard2.setObjectName(u"widgetKeyboard2")
        self.widgetKeyboard2.setGeometry(QRect(0, 140, 480, 135))
        self.widgetKeyboard2.setStyleSheet(u"background-color: rgb(234, 234, 234);")
        self.createFolderBtn = QPushButton(self.page_4)
        self.createFolderBtn.setObjectName(u"createFolderBtn")
        self.createFolderBtn.setGeometry(QRect(360, 100, 111, 31))
        self.createFolderBtn.setStyleSheet(u"border-radius: 20px;\n"
"background-color: #00007f;\n"
"color: white;\n"
"border: none;\n"
"border-radius: 15px;\n"
"")
        self.stackedWidget.addWidget(self.page_4)
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
        self.inputPlace.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ej: Colegio La Rosa", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Nombre de la muestra</p></body></html>", None))
        self.nextBtn.setText(QCoreApplication.translate("MainWindow", u"Siguiente", None))
        self.itRainedBtn.setText(QCoreApplication.translate("MainWindow", u"\u00bfLlovi\u00f3 recientemente?", None))
        self.prevBtn.setText(QCoreApplication.translate("MainWindow", u"Anterior", None))
        self.gpsBtn.setText(QCoreApplication.translate("MainWindow", u"Localizar con GPS", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Latitud, longitud</p></body></html>", None))
        self.saveBtn.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.selectFolderBtn.setText(QCoreApplication.translate("MainWindow", u"Seleccionar carpeta", None))
        self.folderLbl.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Carpeta:</p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Origen o fuente de la muestra", None))
        self.setManualLocationBtn.setText(QCoreApplication.translate("MainWindow", u"Ingresar manualmente", None))
        self.originBtn.setText(QCoreApplication.translate("MainWindow", u"Escoja una opci\u00f3n", None))
        self.openCreateFolderBtn.setText(QCoreApplication.translate("MainWindow", u"Crear una nueva carpeta", None))
        self.emptyFoldersNoticeLbl.setText(QCoreApplication.translate("MainWindow", u"No hay carpetas guardadas", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Nombre</p></body></html>", None))
        self.folderName.setText("")
        self.folderName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ej: Muestras Colegio La Rosa", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">Nueva carpeta</p></body></html>", None))
        self.createFolderBtn.setText(QCoreApplication.translate("MainWindow", u"Crear", None))
    # retranslateUi

