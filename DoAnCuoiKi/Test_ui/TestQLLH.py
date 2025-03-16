import sys

from PyQt6.QtWidgets import QApplication, QMainWindow

from DoAnCuoiKi.Ui.ui_QuanLyLichHen.QLLHExt import QLLHExt

app=QApplication(sys.argv)
mainwinddow=QMainWindow()
myui=QLLHExt()
myui.setupUi(mainwinddow)
myui.showWindow()
app.exec()