import sys

from PyQt6.QtWidgets import QApplication, QMainWindow

from DoAnCuoiKi.Ui.ui_Qr.qrExt import QrExt

app=QApplication(sys.argv)
mainwinddow=QMainWindow()
myui=QrExt()
myui.setupUi(mainwinddow)
myui.showWindow()
app.exec()