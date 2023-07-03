from PySide6.QtWidgets import QApplication
import sys
from interfaz import App

if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec())

