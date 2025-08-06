from PySide2.QtWidgets import QMainWindow, QStackedLayout, QVBoxLayout, QWidget, QGridLayout, QSizePolicy
from PySide2.QtCore import QSize, QThread, Signal, Qt
from PySide2.QtGui import QIcon
from PySide2 import QtCore
from src.views.ui_Save import Ui_MainWindow
from src.widgets.KeyboardWidget import KeyboardWidget
from src.widgets.PopupWidget import PopupWidgetInfo, LoadingPopupWidget, PopupWidget
from src.widgets.FolderWidget import FolderWidget
from .ManualGPSPopup import SetManualLocationWidget
from .ItRainedSelectPopup import ItRainedSelectPopup
from .OriginSelectList import OriginSelectList
from src.model.Models import LoteModel, WaterQualityParams
from src.model.WaterQualityDB import WaterDataBase
from src.model.SensorData import SensorData
from src.config.Constants import Constants
from src.package.Navigator import Navigator
from datetime import datetime
import time
import subprocess

class LocationdWorker(QThread):
    location_result = Signal(list)

    def __init__(self):
        super(LocationdWorker, self).__init__()

    def run(self):
        self.running_state = True
        try:
            subprocess.run("sudo systemctl stop gpsd.socket", shell=True)
            time.sleep(0.5)
            subprocess.run(
                "sudo gpsd /dev/ttyS0 -F /var/run/gpsd.sock", shell=True)
            time.sleep(0.5)
            import gps
            session = gps.gps(mode=gps.WATCH_ENABLE)
        except:
            self.location_result.emit(['error'])
            self.running_state = False
        latitude: float = None
        longitude: float = None
        time_count = 0
        time_period = 2
        while self.running_state:
            try:
                if (time_count * time_period >= 60):
                    self.location_result.emit(['time'])
                report = session.next()

                if report['class'] == 'TPV':
                    if hasattr(report, 'lat') and hasattr(report, 'lon'):
                        latitude = float(report.lat)
                        longitude = float(report.lon)
                        self.location_result.emit([latitude, longitude])
                time.sleep(time_period)
                time_count += 1
            except Exception as e:
                self.location_result.emit(['error'])

    def stop(self):
        self.running_state = False
        self.wait()


class SaveDataView(QMainWindow):
    def __init__(self, context, capture_samples: list[SensorData], close_monitoring_callback:callable):
        QMainWindow.__init__(self)
        self.context = context
        self.capture_samples: list[SensorData] = capture_samples
        self.it_rained:str = None
        self.origin:str = None
        self.latitude = None
        self.longitude = None
        self.folder_name: str = None
        self.folder_id: int = None
        self.folders_list: list[LoteModel] = []
        self.close_monitoring_callback:callable = close_monitoring_callback

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui_components()
        self.setup_list()

        self.loading_popup = None
        self.location_worker = LocationdWorker()

        self.ui.backBtn.clicked.connect(self.on_back_clicked)
        self.ui.nextBtn.clicked.connect(self.on_next_clicked)
        self.ui.prevBtn.clicked.connect(self.on_prev_clicked)
        self.ui.itRainedBtn.clicked.connect(self.on_it_rained_clicked)
        self.ui.originBtn.clicked.connect(self.on_origin_clicked)
        self.ui.gpsBtn.clicked.connect(self.on_gps_clicked)
        self.ui.setManualLocationBtn.clicked.connect(self.on_set_manual_location_clicked)
        self.ui.saveBtn.clicked.connect(self.on_save_clicked)
        self.ui.selectFolderBtn.clicked.connect(self.on_select_folder_clicked)
        self.ui.openCreateFolderBtn.clicked.connect(
            self.on_open_create_folder_clicked)
        self.ui.createFolderBtn.clicked.connect(self.on_create_folder_clicked)

        self.ui.verticalSlider.valueChanged.connect(self.slider_value_changed)
        self.scrollBar.rangeChanged.connect(self.adjust_slider_range)
        self.scrollBar.valueChanged.connect(self.scroll_value_changed)

        self.location_worker.location_result.connect(
            self.handle_location_result)

    def ui_components(self):
        icon = QIcon('./src/resources/icons/back.png')
        self.ui.backBtn.setIcon(icon)
        self.ui.backBtn.setIconSize(QSize(30, 30))
        self.ui.stackedWidget.setCurrentIndex(0)

        self.keyboard = KeyboardWidget(self.ui.inputPlace)
        layout = QStackedLayout(self.ui.widgetKeyboard)
        layout.addWidget(self.keyboard)
        self.ui.widgetKeyboard.setLayout(layout)

        self.keyboard2 = KeyboardWidget(self.ui.folderName)
        layout = QStackedLayout(self.ui.widgetKeyboard2)
        layout.addWidget(self.keyboard2)
        self.ui.widgetKeyboard2.setLayout(layout)

        self.scrollBar = self.ui.scrollArea.verticalScrollBar()
        self.ui.verticalSlider.setRange(
            self.scrollBar.minimum(), self.scrollBar.maximum())
        self.ui.emptyFoldersNoticeLbl.hide()
        self.ui.verticalSlider.hide()

    def on_gps_clicked(self):
        self.loading_popup = LoadingPopupWidget(
            context=self.context, text='Localizando...')
        self.loading_popup.show()
        if not self.location_worker.isRunning():
            self.location_worker.start()

    def handle_location_result(self, location):
        self.location_worker.stop()
        self.loading_popup.close_and_delete()
        if (len(location) == 1):
            if (location[0] == 'error'):
                self.show_dialog_error('Error al intentar localizar.')
                return
            elif (location[0] == 'time'):
                self.show_dialog_error(
                    'Tiempo de espera de<br>localización expirado.')
                return
        self.set_location(location[0], location[1])
        self.show_dialog_error('Localización completada.')

    def set_location(self, latitude:float, longitude:float):
        self.latitude = latitude
        self.longitude = longitude
        self.ui.label_4.setText(f'{self.latitude} , {self.longitude}')
        self.ui.label_4.setAlignment(QtCore.Qt.AlignCenter)
    
    def on_set_manual_location_clicked(self):
        set_location_popup = SetManualLocationWidget(context=self.context, set_location=self.set_location)
        set_location_popup.show()

    def on_back_clicked(self):
        self.show_dialog()

    def close_view(self):
        Navigator.pop(context=self.context, view=self)

    def on_next_clicked(self):
        place = self.ui.inputPlace.text().strip()
        if (place == ''):
            self.show_dialog_error(error='Ingrese un nombre válido')
            return
        if not place.replace(" ", "").isalnum():
            self.show_dialog_error(error='El nombre no puede tener<br>carácteres especiales')
            return
        if self.it_rained == None:
            self.show_dialog_error(error='Escoja una opción en el apartado<br>de lluvia')
            return
        self.ui.stackedWidget.setCurrentIndex(1)

    def on_prev_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def on_select_folder_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def on_open_create_folder_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def on_create_folder_clicked(self):
        name = self.ui.folderName.text().strip()
        if name == "":
            self.show_dialog_error(error='Ingrese el nombre de<br>la carpeta')
            return
        if self.verify_repeated_lote_name(name):
            self.show_dialog_error(error='Ya existe una carpeta con<br>este nombre')
            return
        self.folder_name = name
        self.ui.folderLbl.setText(name)
        self.ui.folderLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.folder_id = None
        self.ui.stackedWidget.setCurrentIndex(1)

    def show_dialog_error(self, error: str):
        dialog = PopupWidgetInfo(context=self.context, text=error)
        dialog.show()

    def show_dialog(self):
        def on_yes():
            if self.location_worker.isRunning():
                self.location_worker.stop()
            self.close_view()

        def on_no():
            pass
        dialog = PopupWidget(context=self.context, yes_callback=on_yes, no_callback=on_no,
                             text='No se han guardado los datos<br>¿Desea salir?')
        dialog.show()

    def on_save_clicked(self):
        if (self.origin == None):
            self.show_dialog_error(error='Seleccione el origen de la muestra')
            return
        if (not (self.latitude and self.longitude)):
            self.show_dialog_error(error='Realice la localización')
            return
        if (not self.folder_name):
            self.show_dialog_error(error='Seleccione una carpeta')
            return
        
        place = self.ui.inputPlace.text().strip()

        dtatetime_now = datetime.now()
        format_date = dtatetime_now.strftime("%Y-%m-%d")
        hour = dtatetime_now.strftime("%H:%M:%S")

        if self.folder_id:
            lote_id = self.folder_id
        else:
            lote = LoteModel(
                name=self.folder_name,
                creation_date=format_date,
                creation_hour=str(hour),
                last_add_date=format_date,
                last_add_hour=str(hour),
            )
            lote_id = WaterDataBase.insert_lote(lote)

        counter = 0
        for sample in self.capture_samples:
            sample_name = place if counter == 0 else f"{place} {counter}"
            params = WaterQualityParams(
                name=sample_name,
                device_id=Constants.DEVICE_ID,
                latitude=self.latitude,
                longitude=self.longitude,
                date=format_date,
                hour=str(hour),
                sample_origin=self.origin,
                it_rained=self.it_rained,
                upload_state=0,
                lote_id=lote_id,
                conductivity=sample.conductivity,
                oxygen=sample.oxygen,
                ph=sample.ph,
                temperature=sample.temperature,
                tds=sample.tds,
                turbidity=sample.turbidity,
                battery=sample.battery
            )
            WaterDataBase.insert_water_param(params)
            counter += 1

        message = "La muestra se guardó exitosamente" if len(self.capture_samples) == 1 else "Las muestras se guardaron exitosamente"
        self.close_monitoring_callback()
        finish_popup = PopupWidgetInfo(
            context=self.context, text=message, on_click=self.close_view, is_warning=False)
        finish_popup.show()

###### FUNCIONES DE POPUP DE LLUVIA ################
    def on_it_rained_clicked(self):
        def set_it_rained(value:str):
            self.it_rained = value
            self.ui.itRainedBtn.setText(f'¿Llovió recientemente?: {value}')
        popup = ItRainedSelectPopup(context=self.context, selected=self.it_rained, on_click=set_it_rained)
        popup.show()
        
###### FUNCIONES DE SELECCION DE ORIGEN ################
    def on_origin_clicked(self):
        def set_origin(value:str):
            self.origin = value
            self.ui.originBtn.setText(value)
        view = OriginSelectList(context=self.context, on_select_origin=set_origin)
        Navigator.push(context=self.context, view=view)
        
###### FUNCIONES DE SELECCION DE LOTES ################
    def load_data(self):
        self.folders_list = WaterDataBase.get_lotes()

    def on_push_folder_widget(self, id: int, name: str):
        self.folder_id = id
        self.folder_name = name
        self.ui.folderLbl.setText(name)
        self.ui.folderLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.ui.stackedWidget.setCurrentIndex(1)

    def setup_list(self):
        self.load_data()

        if len(self.folders_list) == 0:
            self.ui.emptyFoldersNoticeLbl.show()
            self.ui.verticalSlider.hide()
            return

        # Crear el contenedor principal y el layout vertical
        container_widget = QWidget()
        main_layout = QVBoxLayout(container_widget)
        # Alinear contenido en la parte superior
        main_layout.setAlignment(Qt.AlignTop)
        main_layout.setSpacing(10)

        # Crear el layout en cuadrícula
        grid_layout = QGridLayout()
        grid_layout.setSpacing(10)

        num_cols = 3  # Número de columnas
        for i, product in enumerate(self.folders_list):
            # Crear y configurar el widget
            product_widget = FolderWidget(
                id=product.id, name=product.name, description=product.description, on_push=self.on_push_folder_widget)
            product_widget.setFixedSize(133, 100)  # Fijar tamaño del widget
            product_widget.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

            # Calcular la fila y columna
            row = i // num_cols
            col = i % num_cols

            # Establecer tamaño mínimo para filas y columnas
            grid_layout.setRowMinimumHeight(row, 100)
            grid_layout.setColumnMinimumWidth(col, 133)

            # Agregar el widget al layout
            grid_layout.addWidget(product_widget, row, col)

        self.total_rows = (len(self.folders_list) + num_cols - 1) // num_cols
        # Agregar el layout en cuadrícula al layout principal
        main_layout.addLayout(grid_layout)

        # Ajustar el contenedor dentro del ScrollArea
        self.ui.scrollArea.setWidget(container_widget)
        self.ui.scrollArea.setWidgetResizable(True)

    def slider_value_changed(self, value):
        self.scrollBar.setValue(value)

    def adjust_slider_range(self, minValue, maxValue): 
        if maxValue > minValue:  # Solo mostramos el slider si hay algo que desplazar
            self.ui.verticalSlider.show()
            self.ui.verticalSlider.setRange(minValue, maxValue)
            
            # Definir filas visibles en la UI
            visible_rows = 3.5  # Ajusta esto según la visibilidad real en la UI
            total_rows = self.total_rows

            if total_rows > visible_rows:
                step_size = max(1, round((maxValue - minValue) / (total_rows - visible_rows)))
            else:
                step_size = max(1, round((maxValue - minValue) / 3))  # Si hay pocas filas, usar un paso más grande
            
            self.ui.verticalSlider.setSingleStep(step_size)
            self.ui.verticalSlider.setPageStep(step_size * 2)  # Ajustar el desplazamiento por página
        else:
            self.ui.verticalSlider.hide()


    def scroll_value_changed(self, value):
        self.ui.verticalSlider.setValue(value)

    #Verify if a lote exist
    def verify_repeated_lote_name(self, name:str):
        name_lw = name.strip().lower()
        is_repeated = False
        for i in range(len(self.folders_list)):
            is_repeated = name_lw == self.folders_list[i].name.lower()
            if is_repeated:
                break
        return is_repeated
