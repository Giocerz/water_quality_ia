import sys
import time
from pynput.mouse import Controller, Button
from PySide2 import QtWidgets, QtCore
from PySide2.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PySide2.QtCore import QThread
from src.views.TopBarView.TopBarView import TopBarView
from src.views.MainMenuView.MainMenuView import MainMenuView
from src.logic.PCF8574 import PCF8574


class ButtonListener(QThread):
    def __init__(self, parent=None):
        super(ButtonListener, self).__init__(parent)
        self.running = True
        self.pcf8574 = PCF8574()
        self.base_distance = 1
        self.max_distance = 20  # Velocidad máxima del ratón
        self.acceleration_time = 2000  # Tiempo en milisegundos para alcanzar velocidad máxima
        self.movement_states = {  # Guarda el tiempo de inicio de cada movimiento
            "left": 0,
            "right": 0,
            "up": 0,
            "down": 0
        }
        self.flag_center_clicked = False  
        self.last_press_time = 0  
        self.debounce_time = 50  

    def calculate_speed(self, press_start_time, current_time):
        """ Calcula la velocidad basada en el tiempo transcurrido desde que se presionó el botón. """
        if press_start_time == 0:
            return self.base_distance  # Si no ha sido presionado, usar velocidad mínima
        
        elapsed_time = current_time - press_start_time
        factor = min(elapsed_time / self.acceleration_time, 1)  # Normalizamos el tiempo
        return int(self.base_distance + (self.max_distance - self.base_distance) * factor)

    def run(self):
        mouse_controller = Controller()
        try:
            while self.running:
                _, y = mouse_controller.position  
                current_time = time.time_ns() // 1_000_000  # Convertimos a milisegundos

                # Detectamos si los botones de movimiento están presionados
                moving_left = self.pcf8574.read_P0()
                moving_down = self.pcf8574.read_P1()
                moving_right = self.pcf8574.read_P3()
                moving_up = self.pcf8574.read_P4()

                # Guardamos el tiempo en el que se empezó a presionar cada botón
                if moving_left:
                    if self.movement_states["left"] == 0:
                        self.movement_states["left"] = current_time
                    speed = self.calculate_speed(self.movement_states["left"], current_time)
                    mouse_controller.move(-speed, 0)
                else:
                    self.movement_states["left"] = 0

                if moving_down:
                    if self.movement_states["down"] == 0:
                        self.movement_states["down"] = current_time
                    speed = self.calculate_speed(self.movement_states["down"], current_time)
                    mouse_controller.move(0, speed)
                else:
                    self.movement_states["down"] = 0

                if moving_right:
                    if self.movement_states["right"] == 0:
                        self.movement_states["right"] = current_time
                    speed = self.calculate_speed(self.movement_states["right"], current_time)
                    mouse_controller.move(speed, 0)
                else:
                    self.movement_states["right"] = 0

                if moving_up:
                    if self.movement_states["up"] == 0:
                        self.movement_states["up"] = current_time
                    speed = self.calculate_speed(self.movement_states["up"], current_time)

                    # Asegurar que no pase por debajo de y = 10
                    if y - speed < 10:
                        speed = y - 10  # Ajustar para que solo llegue hasta 10

                    mouse_controller.move(0, -speed)
                else:
                    self.movement_states["up"] = 0


                # Filtrado de rebotes para el clic en P2
                current_time = time.time_ns() // 1_000_000  # Convertimos a milisegundos
                p2_pressed = self.pcf8574.read_P2()

                if p2_pressed and not self.flag_center_clicked:
                    if current_time - self.last_press_time > self.debounce_time:
                        mouse_controller.press(Button.left)
                        self.flag_center_clicked = True
                        self.last_press_time = current_time

                elif not p2_pressed and self.flag_center_clicked:
                    if current_time - self.last_press_time > self.debounce_time:
                        mouse_controller.release(Button.left)
                        self.flag_center_clicked = False
                        self.last_press_time = current_time

                time.sleep(0.01)
        except Exception as e:
            print(f"Error con GPIO: {e}")
        finally:
            self.running = False

    def stop(self):
        self.running = False
        self.wait()

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setFixedSize(480, 320)
        
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        
        self.main_layout = QVBoxLayout(self.central_widget)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)
        
        self.top_bar = QtWidgets.QStackedWidget()
        self.top_bar.setFixedSize(480, 48)  
        self.main_layout.addWidget(self.top_bar)
        
        self.bottom_widget = QtWidgets.QStackedWidget()
        self.bottom_widget.setFixedSize(480, 272)
        self.main_layout.addWidget(self.bottom_widget)
        
        top_bar_view = TopBarView(context= self.bottom_widget)
        self.top_bar.addWidget(top_bar_view)

        main_menu_view = MainMenuView(context= self.bottom_widget)
        self.bottom_widget.addWidget(main_menu_view)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    welcome = MyApp()
    button_listener = ButtonListener()
    button_listener.start()

    widget = QtWidgets.QStackedWidget()
    widget.addWidget(welcome)
    widget.setFixedHeight(320)
    widget.setFixedWidth(480)
    widget.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    widget.setAttribute(QtCore.Qt.WA_TranslucentBackground)
    widget.show()
    try:
        sys.exit(app.exec_())
    except:
        print("Exit")
    finally:
        button_listener.stop()
        pass
