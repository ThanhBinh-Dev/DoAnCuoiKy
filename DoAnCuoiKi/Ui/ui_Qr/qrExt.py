from PyQt6.QtWidgets import QMainWindow
from DoAnCuoiKi.Ui.ui_Qr.qr import Ui_MainWindow

class QrExt(QMainWindow, Ui_MainWindow):  # Kế thừa từ QMainWindow và Ui_MainWindow
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Truyền chính `self`, vì class này là QMainWindow
        self.pushButton.clicked.connect(self.show_login_window)
        self.pushButton_caution.clicked.connect(self.QuayLaiPhieuXacNhan)
    def showWindow(self):
        self.show()

    def show_login_window(self):
        from DoAnCuoiKi.Ui.ui_DangNhap.loginExt import loginExt
        self.close()  # Đóng cửa sổ chính
        self.login_window = QMainWindow()
        self.myui = loginExt()
        self.myui.setupUi(self.login_window)
        self.myui.showWindow()

    def QuayLaiPhieuXacNhan(self):
        """Quay lại giao diện Phiếu Xác Nhận"""
        from DoAnCuoiKi.Ui.ui_PhieuXacNhan.PhieuXacNhanExt import PhieuXacNhanExt  # Import muộn

        self.phieu_xac_nhan_window = PhieuXacNhanExt()
        self.phieu_xac_nhan_window.show()
        self.close()  # Đóng cửa sổ hiện tại
