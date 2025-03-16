from PyQt6.QtWidgets import QMainWindow, QApplication

from DoAnCuoiKy.Ui.ui_BiaChinh.biaExt import biaExt

app=QApplication([])
mainwindow=QMainWindow()
myui=biaExt()
myui.setupUi(mainwindow)
myui.showWindow()
app.exec()