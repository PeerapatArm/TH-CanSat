# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_TH_GS.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
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
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QProgressBar, QPushButton, QSizePolicy, QWidget)

from pyqtgraph import PlotWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1330, 865)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setMaximumSize(QSize(1330, 865))
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(49, 49, 49);")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 140, 1291, 711))
        self.frame.setMinimumSize(QSize(1181, 700))
        self.frame.setMaximumSize(QSize(1320, 1000))
        self.frame.setStyleSheet(u"background-color: rgb(100, 100, 100);\n"
"border-radius: 10px;")
        self.Can_Lat_graph = PlotWidget(self.frame)
        self.Can_Lat_graph.setObjectName(u"Can_Lat_graph")
        self.Can_Lat_graph.setGeometry(QRect(20, 50, 251, 121))
        self.Can_Lat_graph.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.T_Can_Lat = QLabel(self.frame)
        self.T_Can_Lat.setObjectName(u"T_Can_Lat")
        self.T_Can_Lat.setGeometry(QRect(30, 20, 81, 21))
        self.T_Can_Lat.setStyleSheet(u"font: 25 10pt \"Bahnschrift Light SemiCondensed\";\n"
"color: white")
        self.Can_Lat = QLabel(self.frame)
        self.Can_Lat.setObjectName(u"Can_Lat")
        self.Can_Lat.setGeometry(QRect(210, 20, 61, 21))
        self.Can_Lat.setStyleSheet(u"font: 25 10pt \"Bahnschrift Light SemiCondensed\";\n"
"color: white")
        self.Can_Long_graph = PlotWidget(self.frame)
        self.Can_Long_graph.setObjectName(u"Can_Long_graph")
        self.Can_Long_graph.setGeometry(QRect(20, 220, 251, 121))
        self.Can_Long_graph.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.T_Can_Long = QLabel(self.frame)
        self.T_Can_Long.setObjectName(u"T_Can_Long")
        self.T_Can_Long.setGeometry(QRect(30, 190, 81, 21))
        self.T_Can_Long.setStyleSheet(u"font: 25 10pt \"Bahnschrift Light SemiCondensed\";\n"
"color: white")
        self.Can_Long = QLabel(self.frame)
        self.Can_Long.setObjectName(u"Can_Long")
        self.Can_Long.setGeometry(QRect(210, 190, 61, 21))
        self.Can_Long.setStyleSheet(u"font: 25 10pt \"Bahnschrift Light SemiCondensed\";\n"
"color: white")
        self.Can_Temp_graph = PlotWidget(self.frame)
        self.Can_Temp_graph.setObjectName(u"Can_Temp_graph")
        self.Can_Temp_graph.setGeometry(QRect(20, 390, 251, 121))
        self.Can_Temp_graph.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.T_Can_Temp = QLabel(self.frame)
        self.T_Can_Temp.setObjectName(u"T_Can_Temp")
        self.T_Can_Temp.setGeometry(QRect(30, 360, 91, 21))
        self.T_Can_Temp.setStyleSheet(u"font: 25 10pt \"Bahnschrift Light SemiCondensed\";\n"
"color: white")
        self.Can_Temp = QLabel(self.frame)
        self.Can_Temp.setObjectName(u"Can_Temp")
        self.Can_Temp.setGeometry(QRect(210, 360, 61, 21))
        self.Can_Temp.setStyleSheet(u"font: 25 10pt \"Bahnschrift Light SemiCondensed\";\n"
"color: white")
        self.Can_Alt_graph = PlotWidget(self.frame)
        self.Can_Alt_graph.setObjectName(u"Can_Alt_graph")
        self.Can_Alt_graph.setGeometry(QRect(20, 560, 251, 121))
        self.Can_Alt_graph.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.T_Can_Alt = QLabel(self.frame)
        self.T_Can_Alt.setObjectName(u"T_Can_Alt")
        self.T_Can_Alt.setGeometry(QRect(30, 530, 91, 21))
        self.T_Can_Alt.setStyleSheet(u"font: 25 10pt \"Bahnschrift Light SemiCondensed\";\n"
"color: white")
        self.Can_Alt = QLabel(self.frame)
        self.Can_Alt.setObjectName(u"Can_Alt")
        self.Can_Alt.setGeometry(QRect(210, 530, 61, 21))
        self.Can_Alt.setStyleSheet(u"font: 25 10pt \"Bahnschrift Light SemiCondensed\";\n"
"color: white")
        self.Cam = QLabel(self.frame)
        self.Cam.setObjectName(u"Cam")
        self.Cam.setGeometry(QRect(320, 20, 641, 351))
        self.Cam.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.Cam.setIndent(-1)
        self.widget_2 = QWidget(self.frame)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(980, 20, 291, 351))
        self.widget_2.setStyleSheet(u"background-color: rgb(57, 57, 57);")
        self.gridLayout = QGridLayout(self.widget_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.T_ACCX = QLabel(self.widget_2)
        self.T_ACCX.setObjectName(u"T_ACCX")
        self.T_ACCX.setStyleSheet(u"font: 25 10pt \"Yu Mincho Light\";\n"
"color: rgb(255, 255, 255);")
        self.T_ACCX.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.T_ACCX, 0, 0, 1, 1)

        self.ACCX = QLabel(self.widget_2)
        self.ACCX.setObjectName(u"ACCX")
        self.ACCX.setStyleSheet(u"font: 25 10pt \"Yu Mincho Light\";\n"
"color: rgb(255, 255, 255);")
        self.ACCX.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.ACCX, 0, 1, 1, 1)

        self.T_GYRX = QLabel(self.widget_2)
        self.T_GYRX.setObjectName(u"T_GYRX")
        self.T_GYRX.setStyleSheet(u"font: 25 10pt \"Yu Mincho Light\";\n"
"color: rgb(255, 255, 255);")
        self.T_GYRX.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.T_GYRX, 0, 2, 1, 1)

        self.GYRX = QLabel(self.widget_2)
        self.GYRX.setObjectName(u"GYRX")
        self.GYRX.setStyleSheet(u"font: 25 10pt \"Yu Mincho Light\";\n"
"color: rgb(255, 255, 255);")
        self.GYRX.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.GYRX, 0, 3, 1, 1)

        self.T_ACCY = QLabel(self.widget_2)
        self.T_ACCY.setObjectName(u"T_ACCY")
        self.T_ACCY.setStyleSheet(u"font: 25 10pt \"Yu Mincho Light\";\n"
"color: rgb(255, 255, 255);")
        self.T_ACCY.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.T_ACCY, 1, 0, 1, 1)

        self.ACCY = QLabel(self.widget_2)
        self.ACCY.setObjectName(u"ACCY")
        self.ACCY.setStyleSheet(u"font: 25 10pt \"Yu Mincho Light\";\n"
"color: rgb(255, 255, 255);")
        self.ACCY.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.ACCY, 1, 1, 1, 1)

        self.T_GYRY = QLabel(self.widget_2)
        self.T_GYRY.setObjectName(u"T_GYRY")
        self.T_GYRY.setStyleSheet(u"font: 25 10pt \"Yu Mincho Light\";\n"
"color: rgb(255, 255, 255);")
        self.T_GYRY.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.T_GYRY, 1, 2, 1, 1)

        self.GYRY = QLabel(self.widget_2)
        self.GYRY.setObjectName(u"GYRY")
        self.GYRY.setStyleSheet(u"font: 25 10pt \"Yu Mincho Light\";\n"
"color: rgb(255, 255, 255);")
        self.GYRY.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.GYRY, 1, 3, 1, 1)

        self.T_ACCZ = QLabel(self.widget_2)
        self.T_ACCZ.setObjectName(u"T_ACCZ")
        self.T_ACCZ.setStyleSheet(u"font: 25 10pt \"Yu Mincho Light\";\n"
"color: rgb(255, 255, 255);")
        self.T_ACCZ.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.T_ACCZ, 2, 0, 1, 1)

        self.ACCZ = QLabel(self.widget_2)
        self.ACCZ.setObjectName(u"ACCZ")
        self.ACCZ.setStyleSheet(u"font: 25 10pt \"Yu Mincho Light\";\n"
"color: rgb(255, 255, 255);")
        self.ACCZ.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.ACCZ, 2, 1, 1, 1)

        self.T_GYRZ = QLabel(self.widget_2)
        self.T_GYRZ.setObjectName(u"T_GYRZ")
        self.T_GYRZ.setStyleSheet(u"font: 25 10pt \"Yu Mincho Light\";\n"
"color: rgb(255, 255, 255);")
        self.T_GYRZ.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.T_GYRZ, 2, 2, 1, 1)

        self.GYRZ = QLabel(self.widget_2)
        self.GYRZ.setObjectName(u"GYRZ")
        self.GYRZ.setStyleSheet(u"font: 25 10pt \"Yu Mincho Light\";\n"
"color: rgb(255, 255, 255);")
        self.GYRZ.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.GYRZ, 2, 3, 1, 1)

        self.widget_3 = QWidget(self.frame)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(320, 620, 951, 61))
        self.widget_3.setStyleSheet(u"background-color: rgb(57, 57, 57);")
        self.horizontalLayout = QHBoxLayout(self.widget_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Status = QLabel(self.widget_3)
        self.Status.setObjectName(u"Status")

        self.horizontalLayout.addWidget(self.Status)

        self.widget_4 = QWebEngineView(self.frame)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(320, 390, 951, 211))
        self.widget_4.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"")
        self.Team_name = QLabel(self.centralwidget)
        self.Team_name.setObjectName(u"Team_name")
        self.Team_name.setGeometry(QRect(20, 10, 401, 111))
        self.Team_name.setStyleSheet(u"background-color: rgb(100, 100, 100);\n"
"font: 25 36pt \"Bahnschrift Light SemiCondensed\";\n"
"border-radius: 10px;\n"
"color: yellow;")
        self.Team_name.setAlignment(Qt.AlignCenter)
        self.Time = QLabel(self.centralwidget)
        self.Time.setObjectName(u"Time")
        self.Time.setGeometry(QRect(1120, 10, 191, 51))
        self.Time.setStyleSheet(u"background-color: rgb(100, 100, 100);\n"
"font: 25 18pt \"Bahnschrift Light SemiCondensed\";\n"
"border-radius: 10px;\n"
"color: yellow;")
        self.Time.setAlignment(Qt.AlignCenter)
        self.elas = QLabel(self.centralwidget)
        self.elas.setObjectName(u"elas")
        self.elas.setGeometry(QRect(1120, 70, 191, 51))
        self.elas.setStyleSheet(u"background-color: rgb(100, 100, 100);\n"
"font: 25 18pt \"Bahnschrift Light SemiCondensed\";\n"
"border-radius: 10px;\n"
"color: yellow;")
        self.elas.setAlignment(Qt.AlignCenter)
        self.Refresh_butt = QPushButton(self.centralwidget)
        self.Refresh_butt.setObjectName(u"Refresh_butt")
        self.Refresh_butt.setGeometry(QRect(720, 50, 91, 31))
        self.Refresh_butt.setStyleSheet(u"background-color: rgb(100, 100, 100);\n"
"border-radius: 10px;\n"
"font: 25 10pt \"Bahnschrift Light SemiCondensed\";\n"
"color: white")
        self.Clear_butt = QPushButton(self.centralwidget)
        self.Clear_butt.setObjectName(u"Clear_butt")
        self.Clear_butt.setGeometry(QRect(620, 50, 91, 31))
        self.Clear_butt.setStyleSheet(u"background-color: rgb(255, 0, 0);\n"
"border-radius: 10px;\n"
"font: 25 10pt \"Bahnschrift Light SemiCondensed\";\n"
"color: white")
        self.Start_butt = QPushButton(self.centralwidget)
        self.Start_butt.setObjectName(u"Start_butt")
        self.Start_butt.setGeometry(QRect(520, 50, 91, 31))
        self.Start_butt.setStyleSheet(u"background-color: rgb(0, 255, 0);\n"
"border-radius: 10px;\n"
"font: 25 10pt \"Bahnschrift Light SemiCondensed\";\n"
"color: white")
        self.Power_box = QComboBox(self.centralwidget)
        self.Power_box.setObjectName(u"Power_box")
        self.Power_box.setGeometry(QRect(430, 10, 81, 31))
        self.Power_box.setStyleSheet(u"background-color: rgb(100, 100, 100);\n"
"border-radius: 10px;\n"
"font: 25 8pt \"Bahnschrift Light SemiCondensed\";")
        self.Port_box = QComboBox(self.centralwidget)
        self.Port_box.setObjectName(u"Port_box")
        self.Port_box.setGeometry(QRect(430, 50, 81, 31))
        self.Port_box.setStyleSheet(u"background-color: rgb(100, 100, 100);\n"
"border-radius: 10px;")
        self.Send_butt = QPushButton(self.centralwidget)
        self.Send_butt.setObjectName(u"Send_butt")
        self.Send_butt.setGeometry(QRect(730, 10, 81, 31))
        self.Send_butt.setStyleSheet(u"background-color: rgb(0,255,0);\n"
"border-radius: 10px;\n"
"font: 25 10pt \"Bahnschrift Light SemiCondensed\";\n"
"color: white")
        self.CMD_line = QLineEdit(self.centralwidget)
        self.CMD_line.setObjectName(u"CMD_line")
        self.CMD_line.setGeometry(QRect(520, 10, 201, 31))
        self.CMD_line.setStyleSheet(u"background-color: rgb(255,255,255);\n"
"border-radius: 10px;")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(820, 10, 291, 111))
        self.widget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.Can_batt = QProgressBar(self.centralwidget)
        self.Can_batt.setObjectName(u"Can_batt")
        self.Can_batt.setGeometry(QRect(520, 90, 91, 31))
        self.Can_batt.setStyleSheet(u"QProgressBar {\n"
"	border-radius: 5px;\n"
"	background-color: rgb(100,100,100);\n"
"	border: 2px solid white;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"	border-radius: 5px;\n"
"	background-color: rgb(0,255,0);\n"
"	border: 2px solid green;\n"
"}")
        self.Can_batt.setValue(70)
        self.Can_batt.setTextVisible(False)
        self.T_Can_batt = QLabel(self.centralwidget)
        self.T_Can_batt.setObjectName(u"T_Can_batt")
        self.T_Can_batt.setGeometry(QRect(440, 90, 61, 31))
        self.T_Can_batt.setStyleSheet(u"font: 25 12pt \"Bahnschrift Light SemiCondensed\";\n"
"color: white")
        self.Roc_batt = QProgressBar(self.centralwidget)
        self.Roc_batt.setObjectName(u"Roc_batt")
        self.Roc_batt.setGeometry(QRect(720, 90, 91, 31))
        self.Roc_batt.setStyleSheet(u"QProgressBar {\n"
"	border-radius: 5px;\n"
"	background-color: rgb(100,100,100);\n"
"	border: 2px solid white;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"	border-radius: 5px;\n"
"	background-color: rgb(0,255,0);\n"
"	border: 2px solid green;\n"
"}")
        self.Roc_batt.setValue(70)
        self.Roc_batt.setTextVisible(False)
        self.T_Roc_batt = QLabel(self.centralwidget)
        self.T_Roc_batt.setObjectName(u"T_Roc_batt")
        self.T_Roc_batt.setGeometry(QRect(640, 90, 61, 31))
        self.T_Roc_batt.setStyleSheet(u"font: 25 12pt \"Bahnschrift Light SemiCondensed\";\n"
"color: white")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.T_Can_Lat.setText(QCoreApplication.translate("MainWindow", u"Latitude", None))
        self.Can_Lat.setText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.T_Can_Long.setText(QCoreApplication.translate("MainWindow", u"Longtitude", None))
        self.Can_Long.setText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.T_Can_Temp.setText(QCoreApplication.translate("MainWindow", u"Temperature", None))
        self.Can_Temp.setText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.T_Can_Alt.setText(QCoreApplication.translate("MainWindow", u"Altitude", None))
        self.Can_Alt.setText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.Cam.setText("")
        self.T_ACCX.setText(QCoreApplication.translate("MainWindow", u"ACCX", None))
        self.ACCX.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.T_GYRX.setText(QCoreApplication.translate("MainWindow", u"GYRX", None))
        self.GYRX.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.T_ACCY.setText(QCoreApplication.translate("MainWindow", u"ACCY", None))
        self.ACCY.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.T_GYRY.setText(QCoreApplication.translate("MainWindow", u"GYRY", None))
        self.GYRY.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.T_ACCZ.setText(QCoreApplication.translate("MainWindow", u"ACCZ", None))
        self.ACCZ.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.T_GYRZ.setText(QCoreApplication.translate("MainWindow", u"GYRZ", None))
        self.GYRZ.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Status.setText("")
        self.Team_name.setText(QCoreApplication.translate("MainWindow", u"Felix-Space AC", None))
        self.Time.setText(QCoreApplication.translate("MainWindow", u"00:00:00:00", None))
        self.elas.setText(QCoreApplication.translate("MainWindow", u"00:00:00:00", None))
        self.Refresh_butt.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.Clear_butt.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.Start_butt.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.Send_butt.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.T_Can_batt.setText(QCoreApplication.translate("MainWindow", u"CanSat", None))
        self.T_Roc_batt.setText(QCoreApplication.translate("MainWindow", u"Rocket", None))
    # retranslateUi

