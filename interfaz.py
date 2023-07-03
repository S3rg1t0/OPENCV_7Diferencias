from ui_ui_interface import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import QTimer
from PySide6.QtGui import QImage, QPixmap
import cv2
import sys

from busquedaDiferencias import FindDifference


class App(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_foto_referencia.clicked.connect(self.take_photo_ref)
        self.ui.pushButton_foto_comparacion.clicked.connect(self.take_photo_comp)
        self.ui.pushButton_comparar.clicked.connect(self.comparar)
        self.ui.pushButton_refresh.clicked.connect(self.refresh)

        self.cap = cv2.VideoCapture(0)

        if not self.cap.isOpened():
            print("No se pudo abrir la webcam")
            sys.exit()

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(round(1000/30))

    def update_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            return
        self.current_frame = frame

        rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        qt_image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
        self.ui.label_marco.setPixmap(QPixmap.fromImage(qt_image))

    def take_photo_ref(self):
        cv2.imwrite("imagenes/foto_referencia.jpg", self.current_frame)

    def take_photo_comp(self):
        cv2.imwrite("imagenes/foto_comparacion.jpg", self.current_frame)

    def comparar(self):
        self.timer.stop()

        comparador = FindDifference(imagen1="imagenes/foto_referencia.jpg",
                                    imagen2="imagenes/foto_comparacion.jpg")
        imagen = comparador.find()


        rgb_image = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        qt_image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
        self.ui.label_marco.clear()
        self.ui.label_marco.setPixmap(QPixmap.fromImage(qt_image))

    def refresh(self):

        self.timer.start(round(1000/30))

