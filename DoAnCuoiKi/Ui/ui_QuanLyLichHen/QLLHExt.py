from PyQt6.QtWidgets import QHeaderView

from DoAnCuoiKi.Ui.ui_QuanLyLichHen.QuanLyLichHen import Ui_MainWindow


class QLLHExt(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.tableWidgetThongTinLH.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.tableWidgetThongTinDK.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.actionQuayLai.triggered.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.actionThongKe.triggered.connect(lambda: self.stackedWidget.setCurrentIndex(1))

    def showWindow(self):
        self.MainWindow.show()
