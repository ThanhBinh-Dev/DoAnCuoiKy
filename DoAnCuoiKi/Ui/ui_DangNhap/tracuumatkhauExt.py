import traceback

from PyQt6.QtWidgets import QMainWindow, QMessageBox

from DoAnCuoiKi.Library.DataConnector import DataConnector
from DoAnCuoiKi.Ui.ui_DangNhap.tracuumatkhau import Ui_MainWindow



class tracuumatkhauExt(Ui_MainWindow):
    def setupUi(self, MainWindow: QMainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.dc = DataConnector()
        self.mainwindow = None  # Lưu tham chiếu cửa sổ mới
        self.setupSignalAndSlot()

    def setupSignalAndSlot(self):
        self.pushButtonSearch.clicked.connect(self.tracuu_sodienthoai)
        self.pushButtonExit.clicked.connect(self.quaylai_dangnhap)
        self.pushButtonCancel.clicked.connect(self.lam_moi)

    def tracuu_sodienthoai(self):
        try:
            phone_number = self.lineEditSearch.text().strip()
            if not phone_number:
                QMessageBox.warning(None, "Lỗi", "Vui lòng nhập số điện thoại!")
                return
            user = self.dc.get_user_by_phone(phone_number)

            if user:
                self.lineEditTenDangNhap.setText(user["tendangnhap"])
                self.lineEditMatKhau.setText(user["matkhau"])
            else:
                QMessageBox.warning(None, "Lỗi", "Không tìm thấy tài khoản với số điện thoại này!")
        except Exception as e:
            print(traceback.format_exc())

    def lam_moi(self):
        self.lineEditSearch.clear()
        self.lineEditTenDangNhap.clear()
        self.lineEditMatKhau.clear()

    def showWindow(self):
        self.MainWindow.show()

    def quaylai_dangnhap(self):
        from DoAnCuoiKi.Ui.ui_DangNhap.loginExt import loginExt# Import tại đây
        self.MainWindow.close()  # Đóng cửa sổ chính
        mainwindow = QMainWindow()
        self.myui = loginExt()
        self.myui.setupUi(mainwindow)
        self.myui.showWindow() # Ẩn thay vì đóng, tránh mất toàn bộ ứng dụng