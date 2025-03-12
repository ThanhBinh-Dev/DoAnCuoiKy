import json
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMessageBox, QApplication, QMainWindow

from DoAnCuoiKi.Ui.ui_Qr.qr import Ui_MainWindow
from DoAnCuoiKi.Ui.ui_DangNhap.login import Ui_MainWindow1 as Ui_LoginWindow

class QrExt(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.show_login_window)
        self.pushButton_caution.clicked.connect(self.QuayLaiPhieuXacNhan)
    def show_login_window(self):
        """Mở giao diện đăng nhập"""
        self.login_window = QMainWindow()
        self.login_ui = Ui_LoginWindow()
        self.login_ui.setupUi(self.login_window)
        self.login_window.show()
        self.close()

    def QuayLaiPhieuXacNhan(self):
        """Quay lại giao diện Phiếu Xác Nhận"""
        from DoAnCuoiKi.Ui.ui_PhieuXacNhan.PhieuXacNhanExt import PhieuXacNhanExt  # Import muộn
        self.phieu_xac_nhan_window = PhieuXacNhanExt()
        self.phieu_xac_nhan_window.show()
        self.close()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = QrExt()
    window.show()
    sys.exit(app.exec())