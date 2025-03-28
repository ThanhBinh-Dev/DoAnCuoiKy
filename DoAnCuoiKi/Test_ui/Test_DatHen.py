import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from DoAnCuoiKi.Ui.ui_DatHen.DatHenExt import DatHenExt

app=QApplication(sys.argv)
mainwinddow=QMainWindow()
myui=DatHenExt()
myui.setupUi(mainwinddow)
myui.showWindow()
app.exec()