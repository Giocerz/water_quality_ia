import os
from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import QSize
from PySide2.QtGui import QIcon
from src.views.ui_UpdateView import Ui_MainWindow
from src.widgets.PopupWidget import LoadingPopupWidget, PopupWidgetInfo
from src.services.internetService import InternetChecker
from src.services.updateService import UpdateChecker, Updater
from src.logic.AppConstans import AppConstants
from src.package.Navigator import Navigator
from src.package.Timer import Timer

class UpdateView(QMainWindow):
    def __init__(self, context):
        QMainWindow.__init__(self)
        self.context = context
        self.loading_popup:LoadingPopupWidget = None
        self.timer:Timer = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui_components()

        self.internet_checker = InternetChecker()
        self.update_checker = UpdateChecker()
        self.updater = Updater()

        self.internet_checker.connection_status.connect(self.internet_check_result)
        self.update_checker.update_checked.connect(self.update_check_result)
        self.updater.update_finished.connect(self.update_finished_result)
        self.ui.updateBtn.clicked.connect(self.init_updater)
        self.ui.backBtn.clicked.connect(self.on_back_clicked)

    def ui_components(self):
        icon = QIcon('./src/resources/icons/back.png')
        self.ui.backBtn.setIcon(icon)
        self.ui.backBtn.setIconSize(QSize(30, 30))
        self.ui.infoVersion.setText(f'Versión {AppConstants.SOFTWARE_VERSION}')
        self.ui.updateBtn.hide()
    
    def on_back_clicked(self):
        if not self.internet_checker.isRunning():
            self.internet_checker.wait()
        if not self.update_checker.isRunning():
            self.update_checker.wait()
        if not self.updater.isRunning():
            self.updater.wait()
        if self.timer is not None:
            self.timer.cancel()
        Navigator.pop(context= self.context, view=self)
    
    def showEvent(self, event):
        """Muestra el popup de carga después de que la ventana principal sea visible."""
        super(UpdateView, self).showEvent(event)
        self.init_internet_check()
    
    def init_internet_check(self):
        self.loading_popup = LoadingPopupWidget(context=self.context, text="Verificando conexión")
        self.loading_popup.show()
        def start_thread():
            self.internet_checker.start()
        self.timer = Timer(duration=1000, callback=start_thread)
        self.timer.start()
    
    def internet_check_result(self, result):
        self.loading_popup.close_and_delete()
        if not result:
            popup = PopupWidgetInfo(context=self.context, text="No hay conexion a internet")
            popup.show()
            return
        self.init_update_check()
    
    def init_update_check(self):
        self.loading_popup = LoadingPopupWidget(context=self.context, text="Verificando actualizaciones")
        self.loading_popup.show()
        def start_thread():
            self.update_checker.start()
        self.timer = Timer(duration=1000, callback=start_thread)
        self.timer.start()

    def update_check_result(self, result, msg):
        self.loading_popup.close_and_delete()
        if result:
            self.ui.infoLbl.setText('Hay actualizaciones disponibles')
            self.ui.updateBtn.show()
        else: 
            if msg:
                self.ui.infoLbl.setText('Error al verificar actualizaciones')
                popup = PopupWidgetInfo(context=self.context, text=msg)
                popup.show()
    
    def init_updater(self):
        self.loading_popup = LoadingPopupWidget(context=self.context, text="Actualizando")
        self.loading_popup.show()
        def start_thread():
            self.updater.start()
        self.timer = Timer(duration=1000, callback=start_thread)
        self.timer.start()
    
    def update_finished_result(self, result):
        self.loading_popup.close_and_delete()
        if result:
            self.ui.infoLbl.setText('El sistema está actualizado')
            self.ui.updateBtn.hide()
            popup = PopupWidgetInfo(context=self.context, text='Actualización completada, el sistema se<br>reiniciará al presionar Ok', on_click=self.on_reset_clicked, is_warning=False)
            popup.show()
        else: 
            self.ui.infoLbl.setText('Error al actualizar')
            popup = PopupWidgetInfo(context=self.context, text='Ocurrió un error al intentar<br>actualizar')
            popup.show()
        
    def on_reset_clicked(self):
        self.loading_popup = LoadingPopupWidget(context=self.context, text="Reiniciando sistema")
        self.loading_popup.show()
        self.timer = Timer(duration=1000, callback=self.reset)
        self.timer.start()
    
    def reset(self):
        os.system("sudo reboot now")