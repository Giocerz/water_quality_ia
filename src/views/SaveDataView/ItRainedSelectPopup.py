from PySide2.QtWidgets import QGraphicsOpacityEffect, QWidget
from PySide2 import QtCore
from src.views.ui_SelectItRainedPopup import Ui_Form
from src.widgets.PopupWidget import PopupWidgetInfo
#test: failed git pull
class ItRainedSelectPopup(QWidget):
    def __init__(self, context, on_click:callable, selected:str = None):
        super().__init__()
        self.context = context
        self._on_click:callable = on_click
        self._selected:str = selected
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui_components()
        
        self.ui.confirmBtn.clicked.connect(self._on_confirm_clicked)
        self.ui.lblOpacity.mousePressEvent = self._handle_click
        self.ui.yesCheckBox.clicked.connect(self._on_yes_clicked)
        self.ui.noCheckBox.clicked.connect(self._on_no_clicked)
        self.ui.idkCheckBox.clicked.connect(self._on_idk_clicked)

    def ui_components(self):
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.opacity = QGraphicsOpacityEffect()
        self.opacity.setOpacity(0.2)
        self.ui.lblOpacity.setGraphicsEffect(self.opacity)

        if self._selected == 'Si':
            self.ui.yesCheckBox.setChecked(True)
            self.ui.noCheckBox.setChecked(False)
            self.ui.idkCheckBox.setChecked(False)
        elif self._selected == 'No':
            self.ui.yesCheckBox.setChecked(False)
            self.ui.noCheckBox.setChecked(True)
            self.ui.idkCheckBox.setChecked(False)
        elif self._selected == 'No lo sé':
            self.ui.yesCheckBox.setChecked(False)
            self.ui.noCheckBox.setChecked(False)
            self.ui.idkCheckBox.setChecked(True)
        else:
            self.ui.yesCheckBox.setChecked(False)
            self.ui.noCheckBox.setChecked(False)
            self.ui.idkCheckBox.setChecked(False)

        self.setParent(self.context)

    def _on_yes_clicked(self):
        self.ui.yesCheckBox.setChecked(True)
        self.ui.noCheckBox.setChecked(False)
        self.ui.idkCheckBox.setChecked(False)

    def _on_no_clicked(self):
        self.ui.yesCheckBox.setChecked(False)
        self.ui.noCheckBox.setChecked(True)
        self.ui.idkCheckBox.setChecked(False)

    def _on_idk_clicked(self):
        self.ui.yesCheckBox.setChecked(False)
        self.ui.noCheckBox.setChecked(False)
        self.ui.idkCheckBox.setChecked(True)

    def _on_confirm_clicked(self):
        yes_state = self.ui.yesCheckBox.isChecked()
        no_state = self.ui.noCheckBox.isChecked()
        idk_state = self.ui.idkCheckBox.isChecked()
        if not (yes_state or no_state or idk_state):
            popup = PopupWidgetInfo(context=self.context, text='Escoge una opción')
            popup.show()
            return
        if yes_state:
            text = 'Si'
        elif no_state:
            text = 'No'
        else:
            text = 'No lo sé'
        self._on_click(text)
        self.close_and_delete()
    
    def close_and_delete(self):
        self.setParent(None)
        self.deleteLater()
    
    def _handle_click(self, event):
        self.close_and_delete()