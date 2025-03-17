from PyQt6.QtWidgets import QApplication, QMainWindow

<<<<<<< HEAD
from DoAnCuoiKi.Ui.ui_DangNhap.login import Ui_MainWindow
=======
from DoAnCuoiKi.Ui.ui_DangNhap.login import Ui_LoginMainWindow
>>>>>>> 0e380858b4dd3a2896515ea5e2320330f20ed309
from DoAnCuoiKi.Ui.ui_Qr.qr import Ui_MainWindow


class QrExt(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.show_login_window)
<<<<<<< HEAD
        self.pushButton_caution.clicked.connect(self.QuayLaiPhieuXacNhan)
=======
        self.pushButton_caution.clicked.connect(self.return_PhieuXacNhan_window)
>>>>>>> 0e380858b4dd3a2896515ea5e2320330f20ed309

    def show_login_window(self):
        """Mở giao diện đăng nhập"""
        self.login_window = QMainWindow()
<<<<<<< HEAD
        self.login_ui = Ui_MainWindow()
=======
        self.login_ui = Ui_LoginMainWindow()
>>>>>>> 0e380858b4dd3a2896515ea5e2320330f20ed309
        self.login_ui.setupUi(self.login_window)
        self.login_window.show()
        self.close()

<<<<<<< HEAD

    def QuayLaiPhieuXacNhan(self):
=======
    def return_PhieuXacNhan_window(self):
>>>>>>> 0e380858b4dd3a2896515ea5e2320330f20ed309
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
