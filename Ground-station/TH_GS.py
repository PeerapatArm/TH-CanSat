from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui_TH_GS import Ui_MainWindow
from SpaceAc_tools import *
from SpaceAc_tools.Port import Port
from SpaceAc_tools import Clock

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connect_butt()
        self.Port_box = None
        self.refresh()
        self.show()

    def connect_butt(self):
        self.ui.Clear_butt.clicked.connect(self.clear)
        self.ui.Start_butt.clicked.connect(self.start)
        self.ui.Refresh_butt.clicked.connect(self.refresh)

    def refresh(self):
        self.ui.Port_box.clear()
        self.ui.Port_box.addItems(Port.list_port())
        

    def start(self):
        self.ui.Port_box.addItems(Port.list_port())
        self.port = self.ui.Port_box.currentText()
        Window.start(self.port)

    def clear(self):
        print("Clear")

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

    def show_ui(self):
        self.ui_main = MainWindow()
        self.ui_main.ui.Can_batt.setValue(100)
        self.ui_main.ui.Roc_batt.setValue(100)
    #line 120 ใน original

    def set_clock(self):
        self.clock = TimerThread()
        self.clock.carrier1.connect(self.update_clock)
        self.clock.carrier2.connect(self.update_elapsed)
        self.clock.start()

    def update_clock(self,data):
        self.ui_main.ui.Time.setText(data)

    def update_elapsed(self, data):
        self.ui_main.ui.elas.setText(data)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Window = Controller()
    sys.exit(app.exec_())