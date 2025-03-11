from PyQt6 import QtWidgets
from DoAnCuoiKy_Thai.DoAnCuoiKi.Ui.ui_DatHen.DatHen import Ui_MainWindow2 as Ui_DatHen

class DatHenExt(QtWidgets.QMainWindow, Ui_DatHen):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Kết nối nút Đặt Hẹn với hàm mở Phiếu Xác Nhận
        self.pushButton_DatHen.clicked.connect(self.open_PhieuXacNhan)

    def open_PhieuXacNhan(self):
        """Mở giao diện Phiếu Xác Nhận"""
        from DoAnCuoiKy_Thai.DoAnCuoiKi.Ui.ui_PhieuXacNhan.PhieuXacNhanExt import PhieuXacNhanExt  # Import muộn

        self.phieu_xac_nhan_window = PhieuXacNhanExt()
        self.phieu_xac_nhan_window.show()
        self.close()  # Đóng giao diện Đặt Hẹn để tránh trùng giao diện

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = DatHenExt()
    window.show()
    sys.exit(app.exec())
