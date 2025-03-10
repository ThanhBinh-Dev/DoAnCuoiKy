import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from DoAnCuoiKi.Ui.ui_QuanLyKhachHang.QLKHExt import QLKHExt

app=QApplication(sys.argv)
mainwinddow=QMainWindow()
myui=QLKHExt()
myui.setupUi(mainwinddow)
myui.showWindow()
app.exec()