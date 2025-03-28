from PyQt6.QtWidgets import QApplication, QDialog, QVBoxLayout, QCheckBox, QPushButton, QMessageBox
import sys

class ExportDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chọn dữ liệu để xuất Excel")
        self.setMinimumWidth(300)

        layout = QVBoxLayout()

        # Danh sách các trường dữ liệu có thể chọn
        self.fields = {
            "Mã Đơn": "madon",
            "Họ và Tên": "hovaten",
            "Số Điện Thoại Khách hàng": "sdt",
            "Địa Chỉ": "diachi",
            "Nơi khám": "noikham",
            "Ngày khám": "ngaykham",
            "Giờ khám": "giokham",
            "Dịch vụ": "dichvu",
            "Thông tin thêm": "thongtin",
            "Tình trạng": "tinhtrang",
            "Bác sĩ": "bacsi",
            "Số điện thoại bác sĩ": "sdtbacsi",
            "Tên đăng nhập": "tendangnhap",
            "Mật khẩu": "matkhau"
        }

        self.checkboxes = {}  # Lưu các checkbox
        for field in self.fields.keys():
            checkbox = QCheckBox(field)
            layout.addWidget(checkbox)
            self.checkboxes[field] = checkbox

        # Nút Export
        self.btn_export = QPushButton("Xuất Excel")
        layout.addWidget(self.btn_export)

        self.setLayout(layout)

        self.btn_export.clicked.connect(self.on_export)

    def on_export(self):
        selected_fields = [key for key, cb in self.checkboxes.items() if cb.isChecked()]

        if not selected_fields:
            QMessageBox.warning(self, "Thông báo", "Vui lòng chọn ít nhất một trường để xuất.")
            return

        QMessageBox.information(self, "Thành công", f"Bạn đã chọn: {', '.join(selected_fields)}")
        self.accept()

    def get_selected_fields(self):
        return [key for key, cb in self.checkboxes.items() if cb.isChecked()]


# Chạy thử hộp thoại
if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = ExportDialog()
    dialog.exec()
