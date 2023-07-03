# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_interfaceEMjsnr.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"#frame QPushButton{\n"
"padding: 10px;\n"
"border-radius: 5px;\n"
"background-color: rgba(33,43,51,100);\n"
"font: 700 12pt \"Arial\";\n"
"}\n"
"\n"
"\n"
"#frame QPushButton:hover\n"
"{\n"
"background-color: rgb(120,157,186);\n"
"}\n"
"\n"
"#centralwidget {\n"
"background-color: rgb(120,157,150);\n"
"}\n"
"\n"
"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(200, 16777215))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton_foto_referencia = QPushButton(self.frame_3)
        self.pushButton_foto_referencia.setObjectName(u"pushButton_foto_referencia")

        self.verticalLayout_2.addWidget(self.pushButton_foto_referencia)

        self.pushButton_foto_comparacion = QPushButton(self.frame_3)
        self.pushButton_foto_comparacion.setObjectName(u"pushButton_foto_comparacion")

        self.verticalLayout_2.addWidget(self.pushButton_foto_comparacion)

        self.pushButton_comparar = QPushButton(self.frame_3)
        self.pushButton_comparar.setObjectName(u"pushButton_comparar")

        self.verticalLayout_2.addWidget(self.pushButton_comparar)


        self.verticalLayout.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.pushButton_refresh = QPushButton(self.frame_4)
        self.pushButton_refresh.setObjectName(u"pushButton_refresh")

        self.verticalLayout_4.addWidget(self.pushButton_refresh)


        self.verticalLayout.addWidget(self.frame_4)


        self.horizontalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_marco = QLabel(self.frame_2)
        self.label_marco.setObjectName(u"label_marco")

        self.verticalLayout_3.addWidget(self.label_marco)


        self.horizontalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_foto_referencia.setText(QCoreApplication.translate("MainWindow", u"Foto referencia", None))
        self.pushButton_foto_comparacion.setText(QCoreApplication.translate("MainWindow", u"Foto comparaci\u00f3n", None))
        self.pushButton_comparar.setText(QCoreApplication.translate("MainWindow", u"Comparar", None))
        self.pushButton_refresh.setText(QCoreApplication.translate("MainWindow", u"Reiniciar", None))
        self.label_marco.setText("")
    # retranslateUi

