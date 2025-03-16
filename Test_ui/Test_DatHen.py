import sys
from PyQt6.QtWidgets import QApplication, QMainWindow

from DoAnCuoiKy.Ui.ui_DatHen.DatHenExt import DatHenExt

app=QApplication(sys.argv)
mainwinddow=QMainWindow()
myui=DatHenExt()
myui.setupUi(mainwinddow)
myui.showWindow()
app.exec()