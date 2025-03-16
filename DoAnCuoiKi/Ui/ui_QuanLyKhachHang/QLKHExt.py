import functools

from PyQt6.QtWidgets import QPushButton

from DoAnCuoiKi.Library.DataConnector_KH import DataConnector_QLKH
from DoAnCuoiKi.Ui.ui_QuanLyKhachHang.QLKH import Ui_MainWindow

class QLKHExt(Ui_MainWindow):
    def __init__(self):
        self.dc=DataConnector_QLKH()
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalsandSlots()
        self.MacDinhTenVaSDT()
        self.HienThiThongTinLenGiaoDien()
    def showWindow(self):
        self.MainWindow.show()
    def setupSignalsandSlots(self):
        pass
    def MacDinhTenVaSDT(self):
        self.lineEdit_SDT.setText("0972936543")
        sdt=self.lineEdit_SDT.text()
        self.list_info=self.dc.search_info(sdt)
        for info in self.list_info:
            self.label_name.setText(info.hovaten)
    def clearLayout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.clearLayout(item.layout())
    def HienThiThongTinLenGiaoDien(self):
        self.clearLayout(self.verticalLayout)
        for info in self.list_info:
            text_button = f"""
                Ngày khám: {info.ngaykham} 
                Giờ khám: {info.giokham} 
                Dịch vụ: {info.dichvu}
            """
            info_button = QPushButton()
            info_button.setText(text_button)
            info_button.setStyleSheet("background-color: rgb(240,237,237); text-align: left; border-radius:20px;border:1px solid black;font-sizre:18pt")
            info_button.setMinimumHeight(70)
            self.verticalLayout.addWidget(info_button)
            # info_button.clicked.connect(functools.partial(self.xem_chitiet, info))

# Trả tên và SĐT khách hàng mặc định và không cho chỉnh sửa sđt, ngày khám, giờ khám
# Giao diện đăng nhập viết thêm một hàm để lấy số đuôi hoặc số điện thoại khách hàng rồi trả về
# Hỗ trợ sửa tên cho khách hàng
# Hiện danh sách dưới định dạng ngày khám, giờ khám, Dịch Vụ Khám
# Truyền dữ liệu cho combobox
# Hiện thông báo khi nhấn hộp thoại lưu
# Đăng ký hẹn thì kết nối giao diện
# Xóa thì hỗ trợ xóa thông tin ở các hộp được chọn
# Bàn lại với nhóm về tính năng xóa, xóa ở đây có thể hỗ trợ
# Nút caution hỗ trợ thông tin khách hàng
# Import/Export Excel
# Ô để viền đỏ khi chưa được xác nhận
# Ô để viền xanh khi được xác nhận
# Ô để viền xám dày khi đã hoàn tất khám
