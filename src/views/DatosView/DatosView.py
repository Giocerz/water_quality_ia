from PySide2 import QtCore
from PySide2.QtWidgets import QMainWindow, QTableWidgetItem
from PySide2.QtCore import QSize
from PySide2.QtGui import QIcon
from src.views.ui_Datos import Ui_MainWindow
from src.views.GraphView.GraphView import GraphView
from src.widgets.PopupWidget import PopupWidget, PopupWidgetInfo
from src.model.Models import WaterQualityParams
from src.model.WaterQualityDB import WaterDataBase
from src.package.Navigator import Navigator
from src.logic.AppConstans import AppConstants

class DatosView(QMainWindow):
    ELEMENTS_NUMBER = 5
    def __init__(self, context, lote_id:int, update_folder_view:callable):
        QMainWindow.__init__(self)
        self.context = context
        self.lote_id:int = lote_id
        self.data_list:list[WaterQualityParams] = []
        self.update_folder_view:callable = update_folder_view
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui_components()

        self.table_pages:int = 0
        self.total_data_len:int = 0
        self.current_page:int = 0

        colums_labels = ['Nombre', 'T(°C)', 'OD(mg/L)', 'TDS(ppm)', 'pH', 
             'CE(uS/cm)', 'Turb(NTU)', 'Bat(%)', 'Fecha', 'Hora', 
             'Lat', 'Long', 'Origen', '¿Llovió?']
        self.ui.tableWidget.setColumnCount(len(colums_labels))
        self.ui.tableWidget.setHorizontalHeaderLabels(colums_labels)

        # Llenar la tabla con los datos de la base de datos
        self.data_table_controller()

        self.ui.backBtn.clicked.connect(self.on_back_clicked)
        self.ui.deleteBtn.clicked.connect(self.on_delete_clicked)
        self.ui.graphBtn.clicked.connect(self.on_graph_clicked)

        self.ui.horizontalSlider.valueChanged.connect(self.slider_value_changed)

        self.scrollBar.rangeChanged.connect(self.adjust_slider_range)
        self.scrollBar.valueChanged.connect(self.scroll_value_changed)

        self.ui.nextPageBtn.clicked.connect(self.handle_nextPageBtn)
        self.ui.prevPageBtn.clicked.connect(self.handle_prevPageBtn)

    def ui_components(self):
        icon = QIcon('./src/resources/icons/arrowr.png')
        self.ui.nextPageBtn.setIcon(icon)
        self.ui.nextPageBtn.setIconSize(QSize(30, 30))
        icon = QIcon('./src/resources/icons/arrowl.png')
        self.ui.prevPageBtn.setIcon(icon)
        self.ui.prevPageBtn.setIconSize(QSize(30, 30))
        icon = QIcon('./src/resources/icons/back.png')
        self.ui.backBtn.setIcon(icon)
        self.ui.backBtn.setIconSize(QSize(30, 30))
        icon = QIcon('./src/resources/icons/graph.png')
        self.ui.graphBtn.setIcon(icon)
        self.ui.graphBtn.setIconSize(QSize(30, 30))
        icon = QIcon('./src/resources/icons/delete.png')
        self.ui.deleteBtn.setIcon(icon)
        self.ui.deleteBtn.setIconSize(QSize(30, 30))

        self.scrollBar = self.ui.tableWidget.horizontalScrollBar()
        self.ui.horizontalSlider.setRange(self.scrollBar.minimum(), self.scrollBar.maximum())

    def data_table_controller(self):
        import math
        self.data_list = WaterDataBase.get_water_quality_params_by_lote(self.lote_id)
        if len(self.data_list) == 0:
            return
        result = []
        self.total_data_len = len(self.data_list)
        self.table_pages = math.ceil(self.total_data_len / self.ELEMENTS_NUMBER)
        for i in range(self.table_pages):
            sub_list = []
            for j in range(self.ELEMENTS_NUMBER*i, self.ELEMENTS_NUMBER*(i+1)):
                if(j >= len(self.data_list)):
                    break
                sub_list.append(self.data_list[j])
            result.append(sub_list)
        self.data_pages = result
        self.update_page(1)
    
    def handle_nextPageBtn(self):
        self.update_page(self.current_page + 1)

    def handle_prevPageBtn(self):
        self.update_page(self.current_page - 1)
        
    def update_page(self, page):
        self.current_page = page
        if(self.current_page >= len(self.data_pages)):
            label_pages = f"{self.ELEMENTS_NUMBER*self.current_page - (self.ELEMENTS_NUMBER - 1)}-{(self.total_data_len)} de {self.total_data_len}"
        else:
            label_pages = f"{self.ELEMENTS_NUMBER*self.current_page - (self.ELEMENTS_NUMBER - 1)}-{(self.ELEMENTS_NUMBER*self.current_page)} de {self.total_data_len}"
        self.ui.dataCountLbl.setText(label_pages)
        self.ui.dataCountLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.ui.prevPageBtn.setEnabled(not(page == 1))
        self.ui.nextPageBtn.setEnabled(not(page == len(self.data_pages)))
        data = self.data_pages[self.current_page - 1]
        self.load_table_data(data=data)

    def slider_value_changed(self, value):
        self.scrollBar.setValue(value)

    def adjust_slider_range(self, min, max):
        self.ui.horizontalSlider.setRange(min, max)    

    def scroll_value_changed(self, value):
        self.ui.horizontalSlider.setValue(value) 

    def on_back_clicked(self):
        Navigator.pop(context=self.context, view= self)

    def load_table_data(self, data:list[list[WaterQualityParams]]):
        def format_value(value):
            """ Devuelve el valor como string, 'OFF' si es MEASURE_OFF_VALUE, o vacío si es None """
            if value is None:
                return ""
            return "OFF" if value == AppConstants.MEASURE_OFF_VALUE else str(value)
        data_list = data

        self.ui.tableWidget.setRowCount(len(data_list))

        for row_idx, data in enumerate(data_list):
            col = -1
            self.ui.tableWidget.setItem(row_idx, col := col + 1, QTableWidgetItem(str(data.name)))

            # Temperatura
            self.ui.tableWidget.setItem(row_idx, col := col + 1, QTableWidgetItem(format_value(data.temperature)))

            # Oxígeno
            self.ui.tableWidget.setItem(row_idx, col := col + 1, QTableWidgetItem(format_value(data.oxygen)))

            # TDS
            self.ui.tableWidget.setItem(row_idx, col := col + 1, QTableWidgetItem(format_value(data.tds)))

            # pH
            self.ui.tableWidget.setItem(row_idx, col := col + 1, QTableWidgetItem(format_value(data.ph)))

            # Conductividad (calculada como el doble de TDS si TDS no es None ni MEASURE_OFF_VALUE)
            conductivity = "" if data.tds is None else ("OFF" if data.tds == AppConstants.MEASURE_OFF_VALUE else str(data.tds * 2))
            self.ui.tableWidget.setItem(row_idx, col := col + 1, QTableWidgetItem(conductivity))

            # Turbidez
            self.ui.tableWidget.setItem(row_idx, col := col + 1, QTableWidgetItem(format_value(data.turbidity)))

            # Batería
            self.ui.tableWidget.setItem(row_idx, col := col + 1, QTableWidgetItem(format_value(data.battery)))
    
            self.ui.tableWidget.setItem(row_idx, col := col + 1, QTableWidgetItem(str(data.date)))
            self.ui.tableWidget.setItem(row_idx, col := col + 1, QTableWidgetItem(str(data.hour)))
            self.ui.tableWidget.setItem(row_idx, col := col + 1, QTableWidgetItem(str(data.latitude)))
            self.ui.tableWidget.setItem(row_idx, col := col + 1, QTableWidgetItem(str(data.longitude)))

            self.ui.tableWidget.setItem(row_idx, col := col + 1, QTableWidgetItem(str(data.sample_origin)))
            self.ui.tableWidget.setItem(row_idx, col := col + 1, QTableWidgetItem(str(data.it_rained)))

    def on_delete_clicked(self):
        self.show_dialog()
    
    def show_dialog(self):
        def on_yes():
            WaterDataBase.delete_lote(self.lote_id)
            self.update_folder_view()
            self.on_back_clicked()

        def on_no():
            pass
        dialog = PopupWidget(context=self.context, yes_callback=on_yes, no_callback=on_no,
                             text='Está acción ELIMINARÁ el lote<br>¿Esta seguro?')
        dialog.show()

    def has_enough_valid_data(self, data_list: list[WaterQualityParams]) -> bool:
        param_names = ["temperature", "ph", "tds", "conductivity", "oxygen", "turbidity"]
        for param in param_names:
            valid_values = [getattr(d, param) for d in data_list if getattr(d, param) not in (None, AppConstants.MEASURE_OFF_VALUE)]
            if len(valid_values) >= 2:
                return True
        return False

    #FUNCIONES PARA ACCEDER A GRAFICAS
    def on_graph_clicked(self):
        if not self.data_list or not self.has_enough_valid_data(self.data_list):
            popup = PopupWidgetInfo(context=self, text='No hay suficientes datos<br>para generar las gráficas')
            popup.show()
            return
    
        Navigator.push(context=self.context, view=GraphView(context=self.context, water_data_list=self.data_list))