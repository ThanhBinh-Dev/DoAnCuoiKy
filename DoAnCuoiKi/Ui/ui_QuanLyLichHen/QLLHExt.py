from DoAnCuoiKi.Ui.ui_QuanLyLichHen.QuanLyLichHen import Ui_MainWindow


class QLLHExt(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
    def showWindow(self):
        self.MainWindow.show()