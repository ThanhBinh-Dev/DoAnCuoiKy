import json
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMessageBox
from DoAnCuoiKy_Thai.DoAnCuoiKi.Ui.ui_PhieuXacNhan.PhieuXacNhan import Ui_MainWindow
from DoAnCuoiKy_Thai.DoAnCuoiKi.Ui.ui_Qr.qr import Ui_MainWindow as Ui_QrWindow
from DoAnCuoiKy_Thai.DoAnCuoiKi.Ui.ui_Qr.qr import Ui_MainWindow as Ui_QrExtWindow
from DoAnCuoiKy_Thai.DoAnCuoiKi.Ui.ui_Qr.qrExt import QrExt
from DoAnCuoiKy_Thai.DoAnCuoiKi.Ui.ui_DatHen.DatHenExt import DatHenExt


class PhieuXacNhanExt(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.current_customer = None  # Khởi tạo thuộc tính tránh lỗi
        self.load_customer_info()
        self.pushButtonThanhToan.clicked.connect(self.ThanhToan)
        self.pushButton_caution.clicked.connect(self.QuayLaiDatHen)

        # Kiểm tra xem các thành phần giao diện có tồn tại không
        if hasattr(self, 'radioButtonKhamTaiGia') and hasattr(self, 'radioButtonPhongKham'):
            self.radioButtonKhamTaiGia.toggled.connect(
                lambda: self.toggle_radio_button(self.radioButtonKhamTaiGia, self.radioButtonPhongKham))
            self.radioButtonPhongKham.toggled.connect(
                lambda: self.toggle_radio_button(self.radioButtonPhongKham, self.radioButtonKhamTaiGia))

        if hasattr(self, 'checkBox_A') and hasattr(self, 'checkBox_B'):
            self.checkBox_A.toggled.connect(lambda: self.toggle_checkbox(self.checkBox_A, self.checkBox_B))
            self.checkBox_B.toggled.connect(lambda: self.toggle_checkbox(self.checkBox_B, self.checkBox_A))

        if hasattr(self, 'lineEditHovaTen'):
            self.lineEditHovaTen.textChanged.connect(self.prevent_changes)
        if hasattr(self, 'lineEditSoDienThoai'):
            self.lineEditSoDienThoai.textChanged.connect(self.prevent_changes)
        if hasattr(self, 'lineEditDiachi'):
            self.lineEditDiachi.textChanged.connect(self.prevent_changes)
        if hasattr(self, 'lineEditNgayKham'):
            self.lineEditNgayKham.textChanged.connect(self.prevent_changes)
        if hasattr(self, 'lineEditGio'):
            self.lineEditGio.textChanged.connect(self.prevent_changes)
        if hasattr(self, 'lineEditDichVuKham'):
            self.lineEditDichVuKham.textChanged.connect(self.prevent_changes)

    def load_customer_info(self):
        try:
            with open("C:/Users/thain/PycharmProjects/K24406H/DoAnCuoiKy_Thai/DoAnCuoiKi/dataset/Info_Customer.json",
                      "r", encoding="utf-8") as file:
                customers = json.load(file)

            print("Dữ liệu JSON đọc được:", customers)  # In dữ liệu để kiểm tra

            if customers:
                self.current_customer = customers[0]  # Lấy khách hàng đầu tiên
                self.fill_customer_data(self.current_customer)
        except Exception as e:
            print("Lỗi khi đọc JSON:", e)

    def fill_customer_data(self, customer):
        if not self.current_customer:
            return

        self.lineEditHovaTen.setText(customer.get("hovaten", ""))
        self.lineEditSoDienThoai.setText(customer.get("sdt", ""))
        self.lineEditDiachi.setText(customer.get("noikham", ""))
        self.lineEditNgayKham.setText(customer.get("ngaykham", ""))
        self.lineEditGio.setText(customer.get("giokham", ""))
        self.lineEditDichVuKham.setText(customer.get("dichvu", ""))

        if customer.get("diachi") == "Khám Tại Gia":
            self.radioButtonKhamTaiGia.setChecked(True)
            self.radioButtonPhongKham.setCheckable(False)
        else:
            self.radioButtonPhongKham.setChecked(True)
            self.radioButtonKhamTaiGia.setCheckable(False)

        if customer.get('checked_A', False):
            self.checkBox_A.setChecked(True)
            self.checkBox_B.setCheckable(False)
        elif customer.get('checked_B', False):
            self.checkBox_B.setChecked(True)
            self.checkBox_A.setCheckable(False)

        self.set_login_credentials(customer)

    def set_login_credentials(self, customer):
        last_name = customer.get("hovaten", "").split()[-1] if customer.get("hovaten") else "user"
        phone_last3 = customer.get("sdt", "")[-3:] if customer.get("sdt") else "000"
        username = customer.get("sdt", "")
        password = f"@{last_name}{phone_last3}"

        self.lineEditTenDangNhap.setText(username)
        self.lineEditMatKhau.setText(password)

        # Cập nhật vào JSON
        self.update_customer_login(username, password)

    def update_customer_login(self, username, password):
        """Ghi hoặc cập nhật thông tin đăng nhập vào JSON"""
        file_path = "C:/Users/thain/PycharmProjects/K24406H/DoAnCuoiKy_Thai/DoAnCuoiKi/dataset/Info_Customer.json"

        try:
            with open(file_path, "r", encoding="utf-8") as file:
                customers = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            customers = []

        # Kiểm tra xem khách hàng đã tồn tại chưa, nếu có thì cập nhật mật khẩu
        customer_found = False
        for customer in customers:
            if customer["sdt"] == username:  # Sử dụng số điện thoại làm key
                customer["tendangnhap"] = username
                customer["matkhau"] = password
                customer_found = True
                break

        # Nếu khách hàng chưa có, thêm mới
        if not customer_found:
            customers.append({
                "hovaten": self.lineEditHovaTen.text(),
                "sdt": username,
                "noikham": self.lineEditDiachi.text(),
                "ngaykham": self.lineEditNgayKham.text(),
                "giokham": self.lineEditGio.text(),
                "dichvu": self.lineEditDichVuKham.text(),
                "tendangnhap": username,
                "matkhau": password
            })

        # Ghi lại dữ liệu vào file JSON
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(customers, file, indent=4, ensure_ascii=False)

        print("Thông tin đăng nhập đã được lưu vào JSON.")

    def prevent_changes(self):
        if self.current_customer:
            QMessageBox.warning(self, "Cảnh báo", "Bạn không được thay đổi Giấy Xác Nhận")
            self.fill_customer_data(self.current_customer)

    def toggle_radio_button(self, selected_button, other_button):
        if selected_button.isChecked():
            other_button.setCheckable(False)
        else:
            other_button.setCheckable(True)

    def toggle_checkbox(self, checked_box, other_box):
        if self.current_customer:
            if self.current_customer.get('checked_A', False):
                self.checkBox_A.setChecked(True)
                self.checkBox_B.setCheckable(False)
            elif self.current_customer.get('checked_B', False):
                self.checkBox_B.setChecked(True)
                self.checkBox_A.setCheckable(False)
            else:
                if checked_box.isChecked():
                    other_box.setCheckable(False)
                else:
                    other_box.setCheckable(True)

    def ThanhToan(self):
        self.qr_window = QrExt()  # Khởi tạo cửa sổ QR đúng cách
        self.qr_window.show()
        self.close()  # Đóng giao diện hiện tại

    def save_customer_data(self):
        """Ghi thông tin khách hàng vào JSON"""
        customer_data = {
            "hovaten": self.lineEditHovaTen.text(),
            "sdt": self.lineEditSoDienThoai.text(),
            "noikham": self.lineEditDiachi.text(),
            "ngaykham": self.lineEditNgayKham.text(),
            "giokham": self.lineEditGio.text(),
            "dichvu": self.lineEditDichVuKham.text(),
            "tendangnhap": self.labelTendangnhap.text(),
            "matkhau": self.labelMatkhau.text()
        }

        try:
            with open("C:/Users/thain/PycharmProjects/K24406H/DoAnCuoiKy_Thai/DoAnCuoiKi/dataset/Info_Customer.json",
                      "r", encoding="utf-8") as file:
                customers = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            customers = []

        # Cập nhật thông tin khách hàng mới vào danh sách
        customers.append(customer_data)

        with open("C:/Users/thain/PycharmProjects/K24406H/DoAnCuoiKy_Thai/DoAnCuoiKi/dataset/Info_Customer.json", "w",
                  encoding="utf-8") as file:
            json.dump(customers, file, indent=4, ensure_ascii=False)

        print("Thông tin khách hàng đã được lưu vào JSON.")

    def QuayLaiDatHen(self):
        # Quay lại giao diện Đặt Hẹn
        self.dat_hen_window = DatHenExt()
        self.dat_hen_window.show()
        self.close()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = PhieuXacNhanExt()
    window.show()
    sys.exit(app.exec())