# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TH-GS.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1330, 865)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(1330, 865))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(49, 49, 49);")
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 140, 1291, 711))
        self.frame.setMinimumSize(QtCore.QSize(1181, 700))
        self.frame.setMaximumSize(QtCore.QSize(1320, 1000))
        self.frame.setStyleSheet("background-color: rgb(100, 100, 100);\n"
"border-radius: 10px;")
        self.frame.setObjectName("frame")
        self.Can_Lat_graph = PlotWidget(self.frame)
        self.Can_Lat_graph.setGeometry(QtCore.QRect(20, 50, 251, 121))
        self.Can_Lat_graph.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Can_Lat_graph.setObjectName("Can_Lat_graph")
        self.T_Can_Lat = QtWidgets.QLabel(self.frame)
        self.T_Can_Lat.setGeometry(QtCore.QRect(30, 20, 81, 21))
        self.T_Can_Lat.setStyleSheet("font: 25 10pt \"Bahnschrift Light SemiCondensed\";\n"
"color: white")
        self.T_Can_Lat.setObjectName("T_Can_Lat")
        self.Can_Lat = QtWidgets.QLabel(self.frame)
        self.Can_Lat.setGeometry(QtCore.QRect(210, 20, 61, 21))
        self.Can_Lat.setStyleSheet("font: 25 10pt \"Bahnschrift Light SemiCondensed\";\n"
"color: white")
        self.Can_Lat.setObjectName("Can_Lat")
        self.Can_Long_graph = PlotWidget(self.frame)
        self.Can_Long_graph.setGeometry(QtCore.QRect(20, 220, 251, 121))
        self.Can_Long_graph.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Can_Long_graph.setObjectName("Can_Long_graph")
        self.T_Can_Long = QtWidgets.QLabel(self.frame)
        self.T_Can_Long.setGeometry(QtCore.QRect(30, 190, 81, 21))
        self.T_Can_Long.setStyleSheet("font: 25 10pt \"Bahnschrift Light SemiCondensed\";\n"
"color: white")
        self.T_Can_Long.setObjectName("T_Can_Long")
        self.Can_Long = QtWidgets.QLabel(self.frame)
        self.Can_Long.setGeometry(QtCore.QRect(210, 190, 61, 21))
        self.Can_Long.setStyleSheet("font: 25 10pt \"Bahnschrift Light SemiCondensed\";\n"
"color: white")
        self.Can_Long.setObjectName("Can_Long")
        self.Can_Temp_graph = PlotWidget(self.frame)
        self.Can_Temp_graph.setGeometry(QtCore.QRect(20, 390, 251, 121))
        self.Can_Temp_graph.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Can_Temp_graph.setObjectName("Can_Temp_graph")
        self.T_Can_Temp = QtWidgets.QLabel(self.frame)
        self.T_Can_Temp.setGeometry(QtCore.QRect(30, 360, 91, 21))
        self.T_Can_Temp.setStyleSheet("font: 25 10pt \"Bahnschrift Light SemiCondensed\";\n"
"color: white")
        self.T_Can_Temp.setObjectName("T_Can_Temp")
        self.Can_Temp = QtWidgets.QLabel(self.frame)
        self.Can_Temp.setGeometry(QtCore.QRect(210, 360, 61, 21))
        self.Can_Temp.setStyleSheet("font: 25 10pt \"Bahnschrift Light SemiCondensed\";\n"
"color: white")
        self.Can_Temp.setObjectName("Can_Temp")
        self.Can_Alt_graph = PlotWidget(self.frame)
        self.Can_Alt_graph.setGeometry(QtCore.QRect(20, 560, 251, 121))
        self.Can_Alt_graph.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Can_Alt_graph.setObjectName("Can_Alt_graph")
        self.T_Can_Alt = QtWidgets.QLabel(self.frame)
        self.T_Can_Alt.setGeometry(QtCore.QRect(30, 530, 91, 21))
        self.T_Can_Alt.setStyleSheet("font: 25 10pt \"Bahnschrift Light SemiCondensed\";\n"
"color: white")
        self.T_Can_Alt.setObjectName("T_Can_Alt")
        self.Can_Alt = QtWidgets.QLabel(self.frame)
        self.Can_Alt.setGeometry(QtCore.QRect(210, 530, 61, 21))
        self.Can_Alt.setStyleSheet("font: 25 10pt \"Bahnschrift Light SemiCondensed\";\n"
"color: white")
        self.Can_Alt.setObjectName("Can_Alt")
        self.Roc_Lat_graph = PlotWidget(self.frame)
        self.Roc_Lat_graph.setGeometry(QtCore.QRect(1020, 50, 251, 121))
        self.Roc_Lat_graph.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Roc_Lat_graph.setObjectName("Roc_Lat_graph")
        self.Roc_Long_graph = PlotWidget(self.frame)
        self.Roc_Long_graph.setGeometry(QtCore.QRect(1020, 220, 251, 121))
        self.Roc_Long_graph.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Roc_Long_graph.setObjectName("Roc_Long_graph")
        self.Roc_Temp_graph = PlotWidget(self.frame)
        self.Roc_Temp_graph.setGeometry(QtCore.QRect(1020, 390, 251, 121))
        self.Roc_Temp_graph.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Roc_Temp_graph.setObjectName("Roc_Temp_graph")
        self.Roc_Alt_graph = PlotWidget(self.frame)
        self.Roc_Alt_graph.setGeometry(QtCore.QRect(1020, 570, 251, 121))
        self.Roc_Alt_graph.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Roc_Alt_graph.setObjectName("Roc_Alt_graph")
        self.T_Roc_Lat = QtWidgets.QLabel(self.frame)
        self.T_Roc_Lat.setGeometry(QtCore.QRect(1030, 20, 81, 21))
        self.T_Roc_Lat.setStyleSheet("font: 25 10pt \"Bahnschrift Light SemiCondensed\";\n"
"color: white")
        self.T_Roc_Lat.setObjectName("T_Roc_Lat")
        self.T_Roc_Long = QtWidgets.QLabel(self.frame)
        self.T_Roc_Long.setGeometry(QtCore.QRect(1030, 190, 81, 21))
        self.T_Roc_Long.setStyleSheet("font: 25 10pt \"Bahnschrift Light SemiCondensed\";\n"
"color: white")
        self.T_Roc_Long.setObjectName("T_Roc_Long")
        self.T_Roc_Temp = QtWidgets.QLabel(self.frame)
        self.T_Roc_Temp.setGeometry(QtCore.QRect(1030, 360, 91, 21))
        self.T_Roc_Temp.setStyleSheet("font: 25 10pt \"Bahnschrift Light SemiCondensed\";\n"
"color: white")
        self.T_Roc_Temp.setObjectName("T_Roc_Temp")
        self.T_Roc_Alt = QtWidgets.QLabel(self.frame)
        self.T_Roc_Alt.setGeometry(QtCore.QRect(1030, 540, 81, 21))
        self.T_Roc_Alt.setStyleSheet("font: 25 10pt \"Bahnschrift Light SemiCondensed\";\n"
"color: white")
        self.T_Roc_Alt.setObjectName("T_Roc_Alt")
        self.Roc_Lat = QtWidgets.QLabel(self.frame)
        self.Roc_Lat.setGeometry(QtCore.QRect(1210, 20, 61, 21))
        self.Roc_Lat.setStyleSheet("font: 25 10pt \"Bahnschrift Light SemiCondensed\";\n"
"color: white")
        self.Roc_Lat.setObjectName("Roc_Lat")
        self.Roc_Long = QtWidgets.QLabel(self.frame)
        self.Roc_Long.setGeometry(QtCore.QRect(1210, 190, 61, 21))
        self.Roc_Long.setStyleSheet("font: 25 10pt \"Bahnschrift Light SemiCondensed\";\n"
"color: white")
        self.Roc_Long.setObjectName("Roc_Long")
        self.Roc_Temp = QtWidgets.QLabel(self.frame)
        self.Roc_Temp.setGeometry(QtCore.QRect(1210, 360, 61, 21))
        self.Roc_Temp.setStyleSheet("font: 25 10pt \"Bahnschrift Light SemiCondensed\";\n"
"color: white")
        self.Roc_Temp.setObjectName("Roc_Temp")
        self.Roc_Alt = QtWidgets.QLabel(self.frame)
        self.Roc_Alt.setGeometry(QtCore.QRect(1210, 540, 61, 21))
        self.Roc_Alt.setStyleSheet("font: 25 10pt \"Bahnschrift Light SemiCondensed\";\n"
"color: white")
        self.Roc_Alt.setObjectName("Roc_Alt")
        self.Team_name = QtWidgets.QLabel(self.centralwidget)
        self.Team_name.setGeometry(QtCore.QRect(20, 10, 401, 111))
        self.Team_name.setStyleSheet("background-color: rgb(100, 100, 100);\n"
"font: 25 36pt \"Bahnschrift Light SemiCondensed\";\n"
"border-radius: 10px;\n"
"color: yellow;")
        self.Team_name.setAlignment(QtCore.Qt.AlignCenter)
        self.Team_name.setObjectName("Team_name")
        self.Time = QtWidgets.QLabel(self.centralwidget)
        self.Time.setGeometry(QtCore.QRect(1120, 10, 191, 51))
        self.Time.setStyleSheet("background-color: rgb(100, 100, 100);\n"
"font: 25 18pt \"Bahnschrift Light SemiCondensed\";\n"
"border-radius: 10px;\n"
"color: yellow;")
        self.Time.setAlignment(QtCore.Qt.AlignCenter)
        self.Time.setObjectName("Time")
        self.elas = QtWidgets.QLabel(self.centralwidget)
        self.elas.setGeometry(QtCore.QRect(1120, 70, 191, 51))
        self.elas.setStyleSheet("background-color: rgb(100, 100, 100);\n"
"font: 25 18pt \"Bahnschrift Light SemiCondensed\";\n"
"border-radius: 10px;\n"
"color: yellow;")
        self.elas.setAlignment(QtCore.Qt.AlignCenter)
        self.elas.setObjectName("elas")
        self.Refresh_butt = QtWidgets.QPushButton(self.centralwidget)
        self.Refresh_butt.setGeometry(QtCore.QRect(720, 50, 91, 31))
        self.Refresh_butt.setStyleSheet("background-color: rgb(100, 100, 100);\n"
"border-radius: 10px;\n"
"font: 25 10pt \"Bahnschrift Light SemiCondensed\";\n"
"color: white")
        self.Refresh_butt.setObjectName("Refresh_butt")
        self.Clear_butt = QtWidgets.QPushButton(self.centralwidget)
        self.Clear_butt.setGeometry(QtCore.QRect(620, 50, 91, 31))
        self.Clear_butt.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"border-radius: 10px;\n"
"font: 25 10pt \"Bahnschrift Light SemiCondensed\";\n"
"color: white")
        self.Clear_butt.setObjectName("Clear_butt")
        self.Start_butt = QtWidgets.QPushButton(self.centralwidget)
        self.Start_butt.setGeometry(QtCore.QRect(520, 50, 91, 31))
        self.Start_butt.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"border-radius: 10px;\n"
"font: 25 10pt \"Bahnschrift Light SemiCondensed\";\n"
"color: white")
        self.Start_butt.setObjectName("Start_butt")
        self.Power_box = QtWidgets.QComboBox(self.centralwidget)
        self.Power_box.setGeometry(QtCore.QRect(430, 10, 81, 31))
        self.Power_box.setStyleSheet("background-color: rgb(100, 100, 100);\n"
"border-radius: 10px;\n"
"font: 25 8pt \"Bahnschrift Light SemiCondensed\";")
        self.Power_box.setObjectName("Power_box")
        self.Power_box.addItem("")
        self.Port_box = QtWidgets.QComboBox(self.centralwidget)
        self.Port_box.setGeometry(QtCore.QRect(430, 50, 81, 31))
        self.Port_box.setStyleSheet("background-color: rgb(100, 100, 100);\n"
"border-radius: 10px;")
        self.Port_box.setObjectName("Port_box")
        self.Send_butt = QtWidgets.QPushButton(self.centralwidget)
        self.Send_butt.setGeometry(QtCore.QRect(730, 10, 81, 31))
        self.Send_butt.setStyleSheet("background-color: rgb(0,255,0);\n"
"border-radius: 10px;\n"
"font: 25 10pt \"Bahnschrift Light SemiCondensed\";\n"
"color: white")
        self.Send_butt.setObjectName("Send_butt")
        self.CMD_line = QtWidgets.QLineEdit(self.centralwidget)
        self.CMD_line.setGeometry(QtCore.QRect(520, 10, 201, 31))
        self.CMD_line.setStyleSheet("background-color: rgb(255,255,255);\n"
"border-radius: 10px;")
        self.CMD_line.setObjectName("CMD_line")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(820, 10, 291, 111))
        self.widget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget.setObjectName("widget")
        self.Can_batt = QtWidgets.QProgressBar(self.centralwidget)
        self.Can_batt.setGeometry(QtCore.QRect(520, 90, 91, 31))
        self.Can_batt.setStyleSheet("QProgressBar {\n"
"    border-radius: 5px;\n"
"    background-color: rgb(100,100,100);\n"
"    border: 2px solid white;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    border-radius: 5px;\n"
"    background-color: rgb(0,255,0);\n"
"    border: 2px solid green;\n"
"}")
        self.Can_batt.setProperty("value", 70)
        self.Can_batt.setTextVisible(False)
        self.Can_batt.setObjectName("Can_batt")
        self.T_Can_batt = QtWidgets.QLabel(self.centralwidget)
        self.T_Can_batt.setGeometry(QtCore.QRect(440, 90, 61, 31))
        self.T_Can_batt.setStyleSheet("font: 25 12pt \"Bahnschrift Light SemiCondensed\";\n"
"color: white")
        self.T_Can_batt.setObjectName("T_Can_batt")
        self.Roc_batt = QtWidgets.QProgressBar(self.centralwidget)
        self.Roc_batt.setGeometry(QtCore.QRect(720, 90, 91, 31))
        self.Roc_batt.setStyleSheet("QProgressBar {\n"
"    border-radius: 5px;\n"
"    background-color: rgb(100,100,100);\n"
"    border: 2px solid white;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    border-radius: 5px;\n"
"    background-color: rgb(0,255,0);\n"
"    border: 2px solid green;\n"
"}")
        self.Roc_batt.setProperty("value", 70)
        self.Roc_batt.setTextVisible(False)
        self.Roc_batt.setObjectName("Roc_batt")
        self.T_Roc_batt = QtWidgets.QLabel(self.centralwidget)
        self.T_Roc_batt.setGeometry(QtCore.QRect(640, 90, 61, 31))
        self.T_Roc_batt.setStyleSheet("font: 25 12pt \"Bahnschrift Light SemiCondensed\";\n"
"color: white")
        self.T_Roc_batt.setObjectName("T_Roc_batt")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.T_Can_Lat.setText(_translate("MainWindow", "Latitude"))
        self.Can_Lat.setText(_translate("MainWindow", "0.00"))
        self.T_Can_Long.setText(_translate("MainWindow", "Longtitude"))
        self.Can_Long.setText(_translate("MainWindow", "0.00"))
        self.T_Can_Temp.setText(_translate("MainWindow", "Temperature"))
        self.Can_Temp.setText(_translate("MainWindow", "0.00"))
        self.T_Can_Alt.setText(_translate("MainWindow", "Altitude"))
        self.Can_Alt.setText(_translate("MainWindow", "0.00"))
        self.T_Roc_Lat.setText(_translate("MainWindow", "Latitude"))
        self.T_Roc_Long.setText(_translate("MainWindow", "Longtitude"))
        self.T_Roc_Temp.setText(_translate("MainWindow", "Tempurature"))
        self.T_Roc_Alt.setText(_translate("MainWindow", "Altitude"))
        self.Roc_Lat.setText(_translate("MainWindow", "0.00"))
        self.Roc_Long.setText(_translate("MainWindow", "0.00"))
        self.Roc_Temp.setText(_translate("MainWindow", "0.00"))
        self.Roc_Alt.setText(_translate("MainWindow", "0.00"))
        self.Team_name.setText(_translate("MainWindow", "Felix-Space AC"))
        self.Time.setText(_translate("MainWindow", "00:00:00:00"))
        self.elas.setText(_translate("MainWindow", "00:00:00:00"))
        self.Refresh_butt.setText(_translate("MainWindow", "Refresh"))
        self.Clear_butt.setText(_translate("MainWindow", "Clear"))
        self.Start_butt.setText(_translate("MainWindow", "Start"))
        self.Power_box.setItemText(0, _translate("MainWindow", "Power on"))
        self.Send_butt.setText(_translate("MainWindow", "Send"))
        self.T_Can_batt.setText(_translate("MainWindow", "CanSat"))
        self.T_Roc_batt.setText(_translate("MainWindow", "Rocket"))

from pyqtgraph import PlotWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

