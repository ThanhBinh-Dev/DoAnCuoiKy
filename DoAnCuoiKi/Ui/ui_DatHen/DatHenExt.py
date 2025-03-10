from DoAnCuoiKi.Library.DataConnector import DataConnector
from DoAnCuoiKi.Ui.ui_DatHen.DatHen import Ui_MainWindow


class DatHenExt(Ui_MainWindow):
    def __init__(self):
        self.dc=DataConnector()
        self.list_times=self.dc.get_all_time()
        self.list_dates = self.dc.get_all_day()
        self.list_serviecs=self.dc.get_all_servieces()
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.show_times()
        self.show_dates()
        self.show_serviecs()
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()
    def setupSignalAndSlot(self):
        self.pushButton_DatHen.clicked.connect(self.XuLyDatHen)
    def show_times(self):
        self.comboBox_GioKham.clear()
        for time in self.list_times:
            self.comboBox_GioKham.addItem(time.giokham)
    def show_dates(self):
        self.comboBox_NgayKham.clear()
        for date in self.list_dates:
            self.comboBox_GioKham.addItem(date.ngaykham)
    def show_serviecs(self):
        self.comboBox_DichVuKham.clear()
        for dichvu in self.list_serviecs:
            self.comboBox_GioKham.addItem(dichvu.dichvu)
    def XuLyDatHen(self):
        pass