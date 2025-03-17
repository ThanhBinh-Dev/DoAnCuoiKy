from PyQt6.QtWidgets import QApplication, QMainWindow

from DoAnCuoiKi.Ui.ui_QuanLyKhachHang.qr import Ui_MainWindow


class QrExt(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
    def showWindow(self):
        self.MainWindow.show()