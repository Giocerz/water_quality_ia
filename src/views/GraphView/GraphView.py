from PySide2.QtWidgets import QMainWindow, QVBoxLayout
from PySide2.QtGui import QIcon
from PySide2.QtCore import QSize
from src.views.ui_Graphics_view import Ui_MainWindow
from src.widgets.PopupWidget import PopupWidgetInfo
from src.model.SensorData import SensorData
from src.model.Models import WaterQualityParams
from src.logic.AppConstans import AppConstants
from src.package.Navigator import Navigator
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

class GraphPreviewView(QMainWindow):
    def __init__(self, context, sensor_data_list:list[SensorData]):
        QMainWindow.__init__(self)
        self.context = context
        self.sensor_data_list:list[SensorData] = sensor_data_list
        self.current_page:int = 0
        self.total_pages:int = 0
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui_components()
        self.load_data()
        self.init_pages()


        self.ui.backBtn.clicked.connect(self.on_back_clicked)
        self.ui.prevPageBtn.clicked.connect(self.on_prev_clicked)
        self.ui.nextPageBtn.clicked.connect(self.on_next_clicked)

    def ui_components(self):
        icon = QIcon('./src/resources/icons/back.png')
        self.ui.backBtn.setIcon(icon)
        self.ui.backBtn.setIconSize(QSize(30, 30))
        icon = QIcon('./src/resources/icons/arrowl.png')
        self.ui.prevPageBtn.setIcon(icon)
        self.ui.prevPageBtn.setIconSize(QSize(30, 30))
        icon = QIcon('./src/resources/icons/arrowr.png')
        self.ui.nextPageBtn.setIcon(icon)
        self.ui.nextPageBtn.setIconSize(QSize(30, 30))
        self.ui.dateLbl.hide()

        self.sc = MplCanvas(self, width=5, height=4, dpi=100)
                # Eliminar márgenes blancos alrededor de la gráfica
        self.sc.figure.tight_layout()
        
        # Crear layout y eliminar márgenes en el widget
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)  # Eliminar márgenes
        layout.setSpacing(0)  # Eliminar espacios entre widgets
        
        layout.addWidget(self.sc)
        self.ui.graphWidget.setLayout(layout)
        # Conectar el evento de clic
        self.sc.mpl_connect("button_press_event", self.on_plot_clicked)

    def on_back_clicked(self):
        Navigator.pop(context=self.context, view=self)

    def on_next_clicked(self):
        if self.current_page == self.total_pages - 1:
            self.current_page = 0
        else:
            self.current_page += 1
        self.update_page()
    
    def on_prev_clicked(self):
        if self.current_page == 0:
            self.current_page = self.total_pages - 1
        else:
            self.current_page -= 1
        self.update_page()

    def load_data(self):
        self.data_values = []  # Lista de listas con los valores de cada parámetro
        self.data_labels_es = []  # Lista con los nombres en español
        self.data_labels_en = []  # Lista con los nombres en inglés (las keys)

        if not self.sensor_data_list:
            popup = PopupWidgetInfo(context=self.context, text='No hay suficientes datos<br>para generar las gráficas')
            popup.show()
            self.on_back_clicked()

        # Diccionario con los nombres en español
        param_names = {
            "temperature": "Temperatura",
            "ph": "pH",
            "tds": "Sólidos Disueltos Totales",
            "conductivity": "Conductividad",
            "oxygen": "Oxígeno Disuelto",
            "turbidity": "Turbidez",
        }

        self.sensor_data_list = list(reversed(self.sensor_data_list))

        for param, label_es in param_names.items():
            values = [getattr(data, param) for data in self.sensor_data_list 
                        if getattr(data, param) is not None and getattr(data, param) != AppConstants.MEASURE_OFF_VALUE]


            if values:  # Solo agregar si hay datos válidos
                self.data_values.append(values)
                self.data_labels_es.append(label_es)  # Nombre en español
                self.data_labels_en.append(param)  # Nombre en inglés (key)

    def init_pages(self):
        self.total_pages = len(self.data_values)
        if self.total_pages == 1:
            self.ui.prevPageBtn.hide()
            self.ui.nextPageBtn.hide()
        self.update_page()
    
    def update_page(self):
        self.ui.titleLbl.setText(self.data_labels_es[self.current_page])
        self.ui.sampleLbl.setText(f'Muestra: ')
        self.ui.valueLbl.setText(f'Valor: ')
        self.canvas_update()
   
    def canvas_update(self):
        x = range(len(self.data_values[self.current_page]))
        y = self.data_values[self.current_page]
        self.sc.axes.clear()
        self.sc.axes.step(x, y, where="post", picker=True, color='#00007f')
        self.sc.axes.set_xticks([]) 
        self.sc.figure.tight_layout()
        self.sc.draw()
    

    def on_plot_clicked(self, event):
        if event.xdata is not None and event.ydata is not None:
            x = int(round(event.xdata))  # Redondear a entero para que sea una muestra
            y = 0
            if x < 0:
                x = 0
            elif x >= len(self.data_values[self.current_page]):
                x = len(self.data_values[self.current_page]) - 1
            y = self.data_values[self.current_page][x]

            # Limpiar líneas anteriores si existen
            if hasattr(self, "vertical_line"):
                self.vertical_line.remove()

            # Dibujar línea vertical en la posición de la muestra
            self.vertical_line = self.sc.axes.axvline(x=x, color='r', linestyle='--', linewidth=1)

            self.ui.sampleLbl.show()
            self.ui.valueLbl.show()
            self.ui.sampleLbl.setText(f'Muestra: {x}')

            param_info = AppConstants.PARAMS_ATTRIBUTES[self.data_labels_en[self.current_page]]
            unit = param_info.get("unit", "")
            if isinstance(unit, list):  # Si hay varias unidades, usar la primera
                unit = unit[0]
            self.ui.valueLbl.setText(f'Valor: {y} {unit}')

            # Actualizar la gráfica
            self.sc.draw()

class GraphView(QMainWindow):
    def __init__(self, context, water_data_list:list[WaterQualityParams]):
        QMainWindow.__init__(self)
        self.context = context
        self.water_data_list:list[SensorData] = water_data_list
        self.current_page:int = 0
        self.total_pages:int = 0
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui_components()
        self.load_data()
        self.init_pages()


        self.ui.backBtn.clicked.connect(self.on_back_clicked)
        self.ui.prevPageBtn.clicked.connect(self.on_prev_clicked)
        self.ui.nextPageBtn.clicked.connect(self.on_next_clicked)

    def ui_components(self):
        icon = QIcon('./src/resources/icons/back.png')
        self.ui.backBtn.setIcon(icon)
        self.ui.backBtn.setIconSize(QSize(30, 30))
        icon = QIcon('./src/resources/icons/arrowl.png')
        self.ui.prevPageBtn.setIcon(icon)
        self.ui.prevPageBtn.setIconSize(QSize(30, 30))
        icon = QIcon('./src/resources/icons/arrowr.png')
        self.ui.nextPageBtn.setIcon(icon)
        self.ui.nextPageBtn.setIconSize(QSize(30, 30))

        self.sc = MplCanvas(self, width=5, height=4, dpi=100)
                # Eliminar márgenes blancos alrededor de la gráfica
        self.sc.figure.tight_layout()
        
        # Crear layout y eliminar márgenes en el widget
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)  # Eliminar márgenes
        layout.setSpacing(0)  # Eliminar espacios entre widgets
        
        layout.addWidget(self.sc)
        self.ui.graphWidget.setLayout(layout)
        # Conectar el evento de clic
        self.sc.mpl_connect("button_press_event", self.on_plot_clicked)

    def on_back_clicked(self):
        Navigator.pop(context=self.context, view=self)

    def on_next_clicked(self):
        if self.current_page == self.total_pages - 1:
            self.current_page = 0
        else:
            self.current_page += 1
        self.update_page()
    
    def on_prev_clicked(self):
        if self.current_page == 0:
            self.current_page = self.total_pages - 1
        else:
            self.current_page -= 1
        self.update_page()

    def load_data(self):
        self.data_values = []  # Lista de listas con los valores de cada parámetro
        self.data_dates = []  # Lista de listas con las fechas de cada muestra
        self.data_labels_es = []  # Lista con los nombres en español
        self.data_labels_en = []  # Lista con los nombres en inglés (las keys)

        # Diccionario con los nombres en español
        param_names = {
            "temperature": "Temperatura",
            "ph": "pH",
            "tds": "Sólidos Disueltos Totales",
            "conductivity": "Conductividad",
            "oxygen": "Oxígeno Disuelto",
            "turbidity": "Turbidez",
        }

        for param, label_es in param_names.items():
            values = []
            dates = []
            
            for data in self.water_data_list:
                value = getattr(data, param)
                if value is not None and value != AppConstants.MEASURE_OFF_VALUE:
                    values.append(value)
                    dates.append(data.date)
            
            if len(values) >= 2:  # Solo agregar si hay al menos 2 valores válidos
                self.data_values.append(values)
                self.data_dates.append(dates)
                self.data_labels_es.append(label_es)  # Nombre en español
                self.data_labels_en.append(param)  # Nombre en inglés (key)

    def init_pages(self):
        self.total_pages = len(self.data_values)
        if self.total_pages == 1:
            self.ui.prevPageBtn.hide()
            self.ui.nextPageBtn.hide()
        self.update_page()
    
    def update_page(self):
        self.ui.titleLbl.setText(self.data_labels_es[self.current_page])
        self.ui.sampleLbl.setText(f'Muestra: ')
        self.ui.valueLbl.setText(f'Valor: ')
        self.ui.dateLbl.setText(f'Fecha: ')
        self.canvas_update()
   
    def canvas_update(self):
        x = range(len(self.data_values[self.current_page]))
        y = self.data_values[self.current_page]
        self.sc.axes.clear()
        self.sc.axes.step(x, y, where="post", picker=True, color='#00007f')
        self.sc.axes.set_xticks([]) 
        self.sc.figure.tight_layout()
        self.sc.draw()
    

    def on_plot_clicked(self, event):
        if event.xdata is not None and event.ydata is not None:
            x = int(round(event.xdata))  # Redondear a entero para que sea una muestra
            y = 0
            if x < 0:
                x = 0
            elif x >= len(self.data_values[self.current_page]):
                x = len(self.data_values[self.current_page]) - 1
            y = self.data_values[self.current_page][x]

            # Limpiar líneas anteriores si existen
            if hasattr(self, "vertical_line"):
                self.vertical_line.remove()

            # Dibujar línea vertical en la posición de la muestra
            self.vertical_line = self.sc.axes.axvline(x=x, color='r', linestyle='--', linewidth=1)

            self.ui.sampleLbl.show()
            self.ui.valueLbl.show()
            self.ui.sampleLbl.setText(f'Muestra: {x + 1}')

            param_info = AppConstants.PARAMS_ATTRIBUTES[self.data_labels_en[self.current_page]]
            unit = param_info.get("unit", "")
            if isinstance(unit, list):  # Si hay varias unidades, usar la primera
                unit = unit[0]
            self.ui.valueLbl.setText(f'Valor: {y} {unit}')
            self.ui.dateLbl.setText(f'Fecha: {self.data_dates[self.current_page][x]}')

            # Actualizar la gráfica
            self.sc.draw()