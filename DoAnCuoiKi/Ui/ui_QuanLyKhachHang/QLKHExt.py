from PyQt6.QtWidgets import QListWidgetItem

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
    def HienThiThongTinLenGiaoDien(self):
        self.listWidget.clear()
        sdt = str(self.lineEdit_SDT.text())
        self.list_info = self.dc.search_info(sdt)
        for info in self.list_info:
            info_item = QListWidgetItem(f"Dịch Vụ: {info.dichvu} "
                                        f"Ngày Khám: {info.ngaykham} "
                                        f"Giờ Khám: {info.giokham}")
            self.listWidget.addItem(info_item)



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
