from PyQt6.QtWidgets import QApplication, QMainWindow

from DoAnCuoiKi.Ui.ui_DangNhap.login import Ui_LoginMainWindow
from DoAnCuoiKi.Ui.ui_Qr.qr import Ui_MainWindow


class QrExt(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.show_login_window)
        self.pushButton_caution.clicked.connect(self.return_PhieuXacNhan_window)

    def show_login_window(self):
        """Mở giao diện đăng nhập"""
        self.login_window = QMainWindow()
        self.login_ui = Ui_LoginMainWindow()
        self.login_ui.setupUi(self.login_window)
        self.login_window.show()
        self.close()

    def return_PhieuXacNhan_window(self):
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
