from PySide2.QtWidgets import QMainWindow, QStackedLayout
from PySide2.QtCore import QSize, Qt
from PySide2.QtGui import QIcon, QStandardItemModel, QStandardItem
from src.views.ui_OriginSelectList import Ui_MainWindow
from src.widgets.PopupWidget import PopupWidgetInfo
from src.widgets.KeyboardWidget import KeyboardWidget
from src.logic.AppConstans import AppConstants
from src.package.Navigator import Navigator

class OriginSelectList(QMainWindow):
    def __init__(self, context, on_select_origin:callable):
        super().__init__()
        self.context = context
        self.__on_select_origin:callable = on_select_origin

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui_components()
        self.set_list()

        self.ui.backBtn.clicked.connect(self.on_back_clicked)
        self.ui.confirmBtn.clicked.connect(self.on_confirm_clicked)
        self.ui.originList.clicked.connect(self.select_origin)
        self.ui.verticalSlider.valueChanged.connect(self.slider_value_changed)
        self.scrollBar.rangeChanged.connect(self.adjust_slider_range)
        self.scrollBar.valueChanged.connect(self.scroll_value_changed)
  

    def ui_components(self):
        icon = QIcon('./src/resources/icons/close.png')
        self.ui.backBtn.setIcon(icon)
        self.ui.backBtn.setIconSize(QSize(30, 30))
        self.scrollBar = self.ui.originList.verticalScrollBar()
        self.ui.verticalSlider.setRange(
            self.scrollBar.minimum(), self.scrollBar.maximum())
        self.ui.verticalSlider.hide()

        self.keyboard = KeyboardWidget(self.ui.inputOrigin)
        layout = QStackedLayout(self.ui.widgetKeyboard)
        layout.addWidget(self.keyboard)
        self.ui.widgetKeyboard.setLayout(layout)

        self.ui.stackedWidget.setCurrentIndex(0)
    
    def set_list(self):
        self.model = QStandardItemModel()
        for origin in AppConstants.WATER_SOURCES:
            standard_item = QStandardItem(origin)
            standard_item.setFlags(standard_item.flags() & ~Qt.ItemIsEditable)
            self.model.appendRow(standard_item)
        self.ui.originList.setModel(self.model)
        
    def on_back_clicked(self):
        Navigator.pop(context=self.context, view=self)

    def slider_value_changed(self, value):
        self.scrollBar.setValue(value)

    def adjust_slider_range(self, min, max):
        self.ui.verticalSlider.show()
        self.ui.verticalSlider.setRange(min, max)

    def scroll_value_changed(self, value):
        self.ui.verticalSlider.setValue(value)
    
    def show_dialog_error(self, error: str):
        dialog = PopupWidgetInfo(context=self.context, text=error)
        dialog.show()

    #FUNCIONES PARA SELECCIONAR ORIGEN
    def select_origin(self):
        indexes = self.ui.originList.selectedIndexes()
        index = indexes[0].row()
        origin = AppConstants.WATER_SOURCES[index]
        if origin != 'Otro':
            self.__on_select_origin(origin)
            self.on_back_clicked()
        else:
            self.open_origin_form()

    def open_origin_form(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def on_confirm_clicked(self):
        origin = self.ui.inputOrigin.text().strip()
        if (origin == ''):
            self.show_dialog_error(error='Ingrese un origen válido')
            return
        if not origin.replace(" ", "").isalnum():
            self.show_dialog_error(error='El origen no puede tener<br>carácteres especiales')
            return
        self.__on_select_origin(f'Otro:{origin}')
        self.on_back_clicked()


