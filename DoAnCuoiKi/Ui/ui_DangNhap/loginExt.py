import traceback

from PyQt6.QtWidgets import QMainWindow, QLineEdit, QMessageBox

from DoAnCuoiKi.Library.DataConnector import DataConnector
from DoAnCuoiKi.Ui.ui_DangNhap.login import Ui_MainWindow
from DoAnCuoiKi.Ui.ui_QuanLyKhachHang.QLKHExt import QLKHExt
from DoAnCuoiKi.Ui.ui_QuanLyLichHen.QLLHExt import QLLHExt

class loginExt(Ui_MainWindow):
    def setupUi(self, MainWindow: QMainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.mainwindow = None  # Lưu tham chiếu cửa sổ mới
        self.setupSignalAndSlot()

    def setupSignalAndSlot(self):
        # Đảm bảo button có thể bật/tắt
        self.pushButtonMatKhau.setCheckable(True)
        # Kết nối sự kiện click
        self.pushButtonMatKhau.toggled.connect(self.togglePasswordVisibility)
        # Quay về giao diện ban đầu
        self.pushButton_caution.clicked.connect(self.quaylai_biachinh)
        # Kết nối giao diện laylaimatkhau
        self.pushButtonQuenMatKhau.clicked.connect(self.hienthi_tracuu_matkhau)
        # Xử lý đăng nhập, chuyển sang giao diện quản lý
        self.pushButtonLogin.clicked.connect(self.xuly_dangnhap)

    def togglePasswordVisibility(self, checked):
        """Hàm thay đổi kiểu hiển thị mật khẩu"""
        if checked:
            self.lineEditMatKhau.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.lineEditMatKhau.setEchoMode(QLineEdit.EchoMode.Password)

    def showWindow(self):
        self.MainWindow.show()

    def quaylai_biachinh(self):
        from DoAnCuoiKi.Ui.ui_BiaChinh.biaExt import biaExt # Import tại đây
        self.MainWindow.close()  # Đóng cửa sổ chính
        mainwindow = QMainWindow()
        self.myui = biaExt()
        self.myui.setupUi(mainwindow)
        self.myui.showWindow()

    # Chuyển sang giao diện quản lý
    def xuly_dangnhap(self):
        try:
            dc = DataConnector()
            username = self.lineEditTenDangNhap.text().strip()
            password = self.lineEditMatKhau.text().strip()
            user_type,sdt = dc.login(username, password)

            if user_type == "customer":
                self.MainWindow.close()
                self.mainwindow = QMainWindow()
                self.myui = QLKHExt(sdt)
                self.myui.setupUi(self.mainwindow)
                self.myui.showWindow()
                if sdt:
                    self.myui.labelSDT.setText(sdt)
            elif user_type == "admin":
                self.MainWindow.close()
                self.mainwindow = QMainWindow()
                self.myui = QLLHExt()
                self.myui.setupUi(self.mainwindow)
                self.myui.showWindow()

            else:
                msg = QMessageBox(self.MainWindow)
                msg.setText("Đăng nhập thất bại. Vui lòng kiểm tra lại!")
                msg.exec()

        except Exception as e:
            print(traceback.format_exc())  # In ra stack trace của lỗi

    # Chuyển sang giao diện tracuu_matkhau
    def hienthi_tracuu_matkhau(self):
        try:
            print("Bắt đầu mở giao diện lấy lại mật khẩu...")  # Debug log
            from DoAnCuoiKi.Ui.ui_DangNhap.tracuumatkhauExt import tracuumatkhauExt  # Import động
            self.MainWindow.hide()  # Thay vì close, dùng hide()
            mainwindow = QMainWindow()
            self.myui = tracuumatkhauExt()
            self.myui.setupUi(mainwindow)
            self.myui.showWindow()
            print("Mở giao diện thành công.")  # Debug log
        except Exception as e:
            print("Lỗi khi mở giao diện lấy lại mật khẩu:", e)
            print(traceback.format_exc())  # In ra stack trace của lỗi