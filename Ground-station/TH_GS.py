from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from ui_TH_GS import Ui_MainWindow
from SpaceAc_tools import *
from SpaceAc_tools.Port import Port
from SpaceAc_tools import Clock
#import cv2

data_dict = {0:'PKG', 1:'ALT', 2:'GYRX', 3:'GYRY', 4:'GYRZ', 5:'ACCX', 6:'ACCY', 7:'ACCZ', 8:'TEM', 9:'LAT', 10:'LNG'}

class MainWindow(QMainWindow, QWidget):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connect_butt()
        self.Port_box = None
        self.refresh()
        self.show()
    
        #self.Worker1 = Worker1()
        #self.Worker1.start()
        #self.Worker1.ImageUpdate.connect(self.ImageUpdateSlot)

    #def ImageUpdateSlot(self, Image):
        #self.ui.Cam.setPixmap(QPixmap.fromImage(Image))

    def connect_butt(self):
        self.ui.Clear_butt.clicked.connect(self.clear)
        self.ui.Start_butt.clicked.connect(self.start)
        self.ui.Refresh_butt.clicked.connect(self.refresh)

    def refresh(self):
        self.ui.Port_box.clear()
        self.ui.Power_box.clear() #baudbox na krub
        self.ui.Port_box.addItems(Port.list_port())
        number =[110,300,600,1200,2400,4800,9600,14400]    
        for i in number:
            self.ui.Power_box.addItem(str(i))
        

    def start(self):
        # self.ui.Port_box.addItems(Port.list_port())
        self.port = self.ui.Port_box.currentText()
        self.baudrate = self.ui.Power_box.currentText()
        Window.start(self.port, self.baudrate, data_dict)

    def clear(self):
        print("Clear")


#class Worker1(QThread):
    #ImageUpdate = pyqtSignal(QImage)
    #def run(self):
        #self.ThreadActive = True
        #Capture = cv2.VideoCapture(0)
        #while self.ThreadActive:
            #ret, frame = Capture.read()
            #if ret:
                #Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                #FlippedImage = cv2.flip(Image, 1)
                #ConvertToQtFormat = QImage(FlippedImage.data , FlippedImage.shape[1], FlippedImage.shape[0], QImage.Format_RGB888)
                #Pic = ConvertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
                #self.ImageUpdate.emit(Pic)
    #def stop(self):
        #self.ThreadActive = False
        #self.quit()

class SerialThread(QThread): #copy จากของเก่า
    carrier1 = QtCore.pyqtSignal(object)
    carrier2 = QtCore.pyqtSignal(object)
    carrier3 = QtCore.pyqtSignal(object)

    def __init__(self, com, baud, key, parent=None) -> None:
        super(SerialThread, self).__init__(parent)
        self.port = Port(com=com, baudrate=baud,
                         end='$', file_name="Project", key=key)
        self.port.connect()

    def __del__(self):
        self.wait()

    def run(self):
        while True:
            try:
                self.pkg = self.port.reading()
            except Exception as e:
                print("packet loss"+e)
                return
            print(self.pkg)
            if isinstance(self.pkg, dict):
                print("[Cansat]", end='\t')
                self.pkg1 = self.pkg
                if float(self.pkg1["LAT"]) != 0 and float(self.pkg1["LNG"]) != 0:
                    self.port.gearthcoord(
                        f"{self.pkg['LNG']},{self.pkg['LAT']},{self.pkg['ALT']}\n")
                self.carrier1.emit(self.pkg1)
    
    def stop(self):
        self._isRunning = False

class TimerThread(QThread):
    carrier1 = QtCore.pyqtSignal(object)
    carrier2 = QtCore.pyqtSignal(object)

    def __init__(self, parent=None) -> None:
        super(TimerThread, self).__init__(parent)
        self.clock = Clock.RTC()

    def __del__(self):
        self.wait()

    def run(self):
        while True:
            self.carrier1.emit(self.clock.time_pc())
            self.carrier2.emit(self.clock.time_elapsed())
            time.sleep(0.001)

    def stop(self):
        self._isRunning = False

class Controller:
    def __init__(self) -> None:
        self.show_ui()
        self.set_clock()
    
    #def show_pic(self):
        #FrameWidth = 641
        #FrameHeight = 350
        #img = cv2.imread("water_test.jpg")
        #img = QPixmap("water_test.jpg")
        #img = cv2.resize(img,(FrameHeight, FrameWidth))
        #self.ui_main.ui.Cam.setPicture(img)

    def show_ui(self):
        self.ui_main = MainWindow()
        self.ui_main.ui.Can_batt.setValue(100)
        self.ui_main.ui.Roc_batt.setValue(100)
        self.cansat ={
            "PKG": [], "ALT": [], "TEM": [], "LAT": [], "LNG": [], "ACCX": [], "ACCY": [], "ACCZ": [], "GYRX": [], "GYRY": [], "GYRZ": []}
    
    def set_ui(self):
        pass

    def start(self, com, baud, key):
        self.serial = SerialThread(com, baud, key)
        self.serial.carrier1.connect(self.update_cansat)
        self.serial.start()

    def set_clock(self):
        self.clock = TimerThread()
        self.clock.carrier1.connect(self.update_clock)
        self.clock.carrier2.connect(self.update_elapsed)
        self.clock.start()
    
    def update_cansat(self, data):
        self.cansat["PKG"].append(int(data["PKG"]))
        self.cansat["ALT"].append(float(data["ALT"]))
        self.cansat["GYRX"].append(float(data["GYRX"]))
        self.cansat["GYRY"].append(float(data["GYRY"]))
        self.cansat["GYRZ"].append(float(data["GYRZ"]))
        self.cansat["ACCX"].append(float(data["ACCX"]))
        self.cansat["ACCY"].append(float(data["ACCY"]))
        self.cansat["ACCZ"].append(float(data["ACCZ"]))
        self.cansat["TEM"].append(float(data["TEM"]))
        self.cansat["LAT"].append(float(data["LAT"]))
        self.cansat["LNG"].append(float(data["LNG"]))
        

        self.ui_main.ui.Can_Alt.setText(str(data["ALT"]))
        self.ui_main.ui.GYRX.setText(str(data["GYRX"]))
        self.ui_main.ui.GYRY.setText(str(data["GYRY"]))
        self.ui_main.ui.GYRZ.setText(str(data["GYRZ"]))
        self.ui_main.ui.ACCX.setText(str(data["ACCX"]))
        self.ui_main.ui.ACCY.setText(str(data["ACCY"]))
        self.ui_main.ui.ACCZ.setText(str(data["ACCZ"]))
        self.ui_main.ui.Can_Temp.setText(str(data["TEM"]))
        self.ui_main.ui.Can_Lat.setText(str(data["LAT"]))
        self.ui_main.ui.Can_Long.setText(str(data["LNG"]))
        

        self.plot(self.ui_main.ui.Can_Alt_graph,
                  self.cansat["PKG"], self.cansat["ALT"])
        self.plot(self.ui_main.ui.Can_GYRX_graph,
                  self.cansat["PKG"], self.cansat["GYRX"])
        self.plot(self.ui_main.ui.Can_GYRY_graph,
                  self.cansat["PKG"], self.cansat["GYRY"])
        self.plot(self.ui_main.ui.Can_GYRZ_graph,
                  self.cansat["PKG"], self.cansat["GYRZ"])
        self.plot(self.ui_main.ui.Can_ACCX_graph,
                  self.cansat["PKG"], self.cansat["ACCX"])
        self.plot(self.ui_main.ui.Can_ACCY_graph,
                  self.cansat["PKG"], self.cansat["ACCY"])
        self.plot(self.ui_main.ui.Can_ACCZ_graph,
                  self.cansat["PKG"], self.cansat["ACCZ"])
        self.plot(self.ui_main.ui.Can_Temp_graph,
                  self.cansat["PKG"], self.cansat["TEM"])
        self.plot(self.ui_main.ui.Can_Lat_graph,
                  self.cansat["PKG"], self.cansat["LAT"])
        self.plot(self.ui_main.ui.Can_Long_graph,
                  self.cansat["PKG"], self.cansat["LNG"])
        
        


    def update_clock(self,data):
        self.ui_main.ui.Time.setText(data)

    def update_elapsed(self, data):
        self.ui_main.ui.elas.setText(data)

    def plot(self, graph, x, y):
        graph.clear()
        if len(x) > 50:
            graph.plot(x[-50:-1], y[-50:-1])
        else:
            graph.plot(x, y)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Window = Controller()
    #Root = MainWindow()
    #Root.show()
    sys.exit(app.exec_())