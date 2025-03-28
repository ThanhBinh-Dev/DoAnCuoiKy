import webbrowser
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QCursor
from PyQt6.QtWidgets import QMainWindow

from DoAnCuoiKi.Ui.ui_BiaChinh.bia import Ui_MainWindow



class biaExt(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlot()

    def showWindow(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        """Kết nối QLabel với sự kiện mở trình duyệt"""
        self.labelWebsite_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.labelWebsite_2.mousePressEvent = self.openWebsite
        """Kết nối giao diện đăng nhập"""
        self.pushButtonDangNhap.clicked.connect(self.hienthi_giaodien_dangnhap)
        self.pushButtonDatLich.clicked.connect(self.hienthi_giaodien_dathen)

    def openWebsite(self, event):
        """Mở trang web khi nhấn vào labelWebsite"""
        webbrowser.open("https://www.drpethouse.com")

    def hienthi_giaodien_dangnhap(self):
        from DoAnCuoiKi.Ui.ui_DangNhap.loginExt import loginExt  # Import tại đây
        self.MainWindow.close()  # Đóng cửa sổ chính
        mainwindow = QMainWindow()
        self.myui = loginExt()
        self.myui.setupUi(mainwindow)
        self.myui.showWindow()

    def hienthi_giaodien_dathen(self):
        from DoAnCuoiKi.Ui.ui_DatHen.DatHenExt import DatHenExt
        self.MainWindow.close()  # Đóng cửa sổ chính
        mainwindow = QMainWindow()
        self.myui = DatHenExt()
        self.myui.setupUi(mainwindow)
        self.myui.showWindow()