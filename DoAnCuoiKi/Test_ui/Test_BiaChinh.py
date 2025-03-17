from PyQt6.QtWidgets import QMainWindow, QApplication

from DoAnCuoiKi.Ui.ui_BiaChinh.biaExt import biaExt

app=QApplication([])
mainwindow=QMainWindow()
myui=biaExt()
myui.setupUi(mainwindow)
myui.showWindow()
app.exec()