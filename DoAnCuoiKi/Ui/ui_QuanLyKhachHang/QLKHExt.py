from DoAnCuoiKi.Ui.ui_QuanLyKhachHang.QLKH import Ui_MainWindow

class QLKHExt(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
    def showWindow(self):
        self.MainWindow.show()


