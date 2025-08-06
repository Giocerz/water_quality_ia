import subprocess
from PySide2.QtCore import QThread, Signal

class UpdateChecker(QThread):
    """ Hilo para verificar si hay una actualización disponible en Git """
    update_checked = Signal(bool, str)  # (True, mensaje) si hay actualización, (False, mensaje) si no

    def run(self):
        try:
            # Obtener los cambios más recientes sin aplicarlos
            subprocess.run(["git", "fetch"], capture_output=True, text=True)
            
            status_output = subprocess.run(
                ["git", "status"],
                capture_output=True,
                text=True
            ).stdout

            if "Your branch is up to date" in status_output:
                self.update_checked.emit(False, "")
            else:
                self.update_checked.emit(True, "")

        except Exception as e:
            self.update_checked.emit(False, f"Error al verificar<br>actualizaciones")

class Updater(QThread):
    update_finished = Signal(bool)  
    def run(self):
        try:
            result = subprocess.run(["git", "pull"], capture_output=True, text=True)

            if result.returncode == 0:
                if "Already up to date." in result.stdout:
                    self.update_finished.emit(True)
                else:
                    self.update_finished.emit(True)
            elif result.returncode == 1:
                self.update_finished.emit(False)

            elif result.returncode == 128:
                self.update_finished.emit(False)
            else:
                self.update_finished.emit(False)
        except Exception as e:
            self.update_finished.emit(False)
