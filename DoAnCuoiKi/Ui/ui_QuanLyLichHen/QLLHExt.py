import json
from datetime import datetime, timedelta

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor, QBrush
from PyQt6.QtWidgets import QHeaderView, QMainWindow, QMessageBox, QTableWidgetItem

from DoAnCuoiKi.Library.DataConnector_QLLH import DataConnector_QLLH
from DoAnCuoiKi.Library.Im_ExportTool import ExportTool
from DoAnCuoiKi.Library.export import ExportDialog
from DoAnCuoiKi.Ui.ui_BiaChinh.biaExt import biaExt
from DoAnCuoiKi.Ui.ui_DatHen.DatHenExt import DatHenExt
from DoAnCuoiKi.Ui.ui_QuanLyLichHen.QuanLyLichHen import Ui_MainWindow
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from PyQt6.QtWidgets import QVBoxLayout

class QLLHExt(Ui_MainWindow):
    def __init__(self):
        #qllh
        self.dc = DataConnector_QLLH()
        self.info_customer = self.dc.get_info_customer()
        self.date_time_list = self.dc.get_date_time_data()
        self.list_dates = self.dc.sort_ngay_kham_con_slot()
        self.list_times = {ngay: self.dc.sort_gio_kham_con_slot_trong_ngay(ngay) for ngay in self.list_dates}
        self.list_services = self.dc.get_all_services()
        self.list_doctor = self.dc.get_all_doctor()
        self.doctor_dict = {doctor.bacsi: doctor.sdtbacsi for doctor in self.list_doctor}
        self.sorted_customers = self.dc.sort_info_customer()
        self.selected = None
        self.current_displayed_customers = {}
        #dashboard
        self.labelSoLieu1 = None
        self.labelSoLieu2 = None
        self.labelSoLieu3 = None
        self.labelTag1 = None
        self.labelTag2 = None
        self.labelTag3 = None

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.tableWidgetThongTinLH.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.tableWidgetThongTinDK.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.tabWidget.setCurrentIndex(self.tabWidget.indexOf(self.tabLichHen))
        self.show_LH_xacnhan_ui()
        self.show_LH_dakham_ui()
        self.process_update_current_displayed_customers()
        self.setupSignalsandSlots()
        self.update_comboBox_NgayHen()
        self.update_ui()
        #dashboard
        self.actionQuayLai.triggered.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.actionThongKe.triggered.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.dashboard_khachhang()
        self.dashboard_LH_homnay()
        self.dashboard_LH_tuan()
        self.bieudoduong()
        self.bieudotron()
    def showWindow(self):
        self.MainWindow.show()
    #qllh
    def hien_thi_lich_hen(self, table_widget,tinhtrang_filter=None):
        self.sorted_customers=  sorted(self.info_customer, key=lambda x:  (x.ngaykham, x.giokham))
        table_widget.clearContents()
        table_widget.setRowCount(0)

        for info_customer in self.sorted_customers:
            if tinhtrang_filter and info_customer.tinhtrang not in tinhtrang_filter:
                continue

            row = table_widget.rowCount()
            table_widget.insertRow(row)

            col_madon = QTableWidgetItem(info_customer.madon)
            col_hovaten = QTableWidgetItem(info_customer.hovaten)
            col_sdt = QTableWidgetItem(str(info_customer.sdt))
            col_ngaykham = QTableWidgetItem(str(info_customer.ngaykham))
            col_giokham = QTableWidgetItem(str(info_customer.giokham))
            col_dichvu = QTableWidgetItem(info_customer.dichvu)
            col_noikham = QTableWidgetItem(info_customer.noikham)
            col_tinhtrang = QTableWidgetItem(info_customer.tinhtrang)
            col_bacsi = QTableWidgetItem(info_customer.bacsi)
            col_sdtbacsi = QTableWidgetItem(info_customer.sdtbacsi)

            table_widget.setItem(row, 0, col_madon)
            table_widget.setItem(row, 1, col_hovaten)
            table_widget.setItem(row, 2, col_sdt)
            table_widget.setItem(row, 3, col_ngaykham)
            table_widget.setItem(row, 4, col_giokham)
            table_widget.setItem(row, 5, col_dichvu)
            table_widget.setItem(row, 6, col_noikham)
            table_widget.setItem(row, 7, col_tinhtrang)
            table_widget.setItem(row, 8, col_bacsi)
            table_widget.setItem(row, 9, col_sdtbacsi)

            if info_customer.tinhtrang == "Chưa Xác Nhận":
                col_tinhtrang.setBackground(Qt.GlobalColor.red)
            elif info_customer.tinhtrang == "Đã Xác Nhận":
                col_tinhtrang.setBackground(QBrush(QColor(153, 225, 255)))
            elif info_customer.tinhtrang == "Đã Khám":
                col_tinhtrang.setBackground(QBrush(Qt.GlobalColor.green))


    def process_update_current_displayed_customers(self):
        for table_widget in [self.tableWidgetThongTinLH, self.tableWidgetThongTinDK]:
            for row in range(table_widget.rowCount()):
                madon_item = table_widget.item(row, 0)
                if madon_item:
                    madon = madon_item.text().strip()
                    for info in self.info_customer:
                        if info.madon == madon:
                            self.current_displayed_customers[madon] = info

    def show_LH_xacnhan_ui(self):
        self.hien_thi_lich_hen(self.tableWidgetThongTinLH, tinhtrang_filter=["Chưa Xác Nhận", "Đã Xác Nhận"])
    def show_LH_dakham_ui(self):
        self.hien_thi_lich_hen(self.tableWidgetThongTinDK, tinhtrang_filter=["Đã Khám"])

    def update_ui(self, tinhtrang=None):
        if tinhtrang == "Đã Xác Nhận":
            self.sort_daxacnhan()
        elif tinhtrang == "Chưa Xác Nhận":
            self.sort_chuaxacnhan()
        elif tinhtrang == "Đã Khám":
            self.show_LH_dakham_ui()
        else:
            self.show_LH_xacnhan_ui()

    def setupSignalsandSlots(self):
        self.pushButtonHienThiTatCaLH.clicked.connect(self.show_LH_xacnhan_ui)
        self.pushButtonRestore.clicked.connect(self.show_LH_dakham_ui)
        self.pushButtonDaXacNhan.clicked.connect(self.sort_daxacnhan)
        self.pushButtonChuaXacNhan.clicked.connect(self.sort_chuaxacnhan)
        self.tableWidgetThongTinLH.itemSelectionChanged.connect(lambda:self.process_show_infor_detail(self.tableWidgetThongTinLH))
        self.tableWidgetThongTinDK.itemSelectionChanged.connect(lambda:self.process_show_infor_detail(self.tableWidgetThongTinDK))
        self.comboBoxBacSi.currentIndexChanged.connect(self.update_sdtbacsi)
        self.pushButtonTimKiem.clicked.connect(self.search_info)
        self.lineEditTimKiem.returnPressed.connect(self.search_info)
        self.pushButtonTimKiemDK.clicked.connect(self.search_info_dk)
        self.lineEditTimKiemDK.returnPressed.connect(self.search_info_dk)
        self.pushButtonLuu.clicked.connect(self.save_change)
        self.pushButtonXoa.clicked.connect(self.delete_appointment)
        self.pushButtonThemLH.clicked.connect(self.open_DatHen_window)
        self.actionExcel_FIle_Export.triggered.connect(self.export_to_excel)
        self.actionExit.triggered.connect(self.sign_out)


    def sort_daxacnhan(self):
        self.hien_thi_lich_hen(self.tableWidgetThongTinLH,tinhtrang_filter=["Đã Xác Nhận"])

    def sort_chuaxacnhan(self):
        self.hien_thi_lich_hen(self.tableWidgetThongTinLH,tinhtrang_filter=["Chưa Xác Nhận"])

    def process_show_infor_detail(self,table_widget):
        index = table_widget.currentRow()
        if index < 0:
            return

        madon_item = table_widget.item(index, 0)
        if not madon_item:
            QMessageBox.warning(self.MainWindow, "Lỗi", "Không tìm thấy mã đơn trong bảng!")
            return

        madon = madon_item.text().strip()
        if madon not in self.current_displayed_customers:
            QMessageBox.warning(self.MainWindow, "Lỗi", f"Không tìm thấy mã đơn: {madon}")
            return

        column_tinhtrang = 7

        for row in range(table_widget.rowCount()):
            for col in range(table_widget.columnCount()):
                if col == column_tinhtrang:  # Bỏ qua cột "Tình trạng"
                    continue
                item = table_widget.item(row, col)
                if item:
                    item.setBackground(QBrush(QColor("#FFFFFF")))

        for col in range(table_widget.columnCount()):
            if col == column_tinhtrang:  # Bỏ qua cột "Tình trạng"
                continue
            item = table_widget.item(index, col)
            if item:
                item.setBackground(QBrush(QColor("#fae38c")))

        info_customer = self.current_displayed_customers[madon]

        self.lineEditKhachHang.setText(info_customer.hovaten)
        self.lineEditSoDienThoaiKH.setText(str(info_customer.sdt))
        self.lineEditDiaChi.setText(info_customer.diachi)
        if info_customer.thongtin == "None":
            info_customer.thongtin = ""
        self.lineEditThongTin.setText(info_customer.thongtin)
        self.comboBoxDichVu.currentText()

        self.comboBoxBacSi.clear()
        self.lineEditsdtbacsi.clear()

        self.comboBoxBacSi.addItem("")
        for doctor in self.list_doctor:
            self.comboBoxBacSi.addItem(doctor.bacsi)

        if info_customer.bacsi and info_customer.bacsi in self.doctor_dict:
            index_bacsi = self.comboBoxBacSi.findText(info_customer.bacsi)
            if index_bacsi != -1:
                self.comboBoxBacSi.setCurrentIndex(index_bacsi)
                self.lineEditsdtbacsi.setText(self.doctor_dict[info_customer.bacsi])
        else:
            self.comboBoxBacSi.setCurrentIndex(0)
            self.lineEditsdtbacsi.clear()

        # Cập nhật comboBox ngày hẹn
        self.comboBoxNgayHen.clear()
        self.comboBoxNgayHen.addItems(self.list_dates)
        self.comboBoxNgayHen.setCurrentIndex(-1)

        index_ngay = self.comboBoxNgayHen.findText(str(info_customer.ngaykham))
        if index_ngay != -1:
            self.comboBoxNgayHen.setCurrentIndex(index_ngay)
        else:
            QMessageBox.warning(self.MainWindow, "Lỗi", f"Ngày {info_customer.ngaykham} không có trong danh sách!")

        # Cập nhật giờ khám theo ngày
        self.update_gio_kham()
        selected_date = info_customer.ngaykham
        selected_time = info_customer.giokham

        self.comboBoxGio.clear()
        if selected_date in self.list_times:
            available_times = self.list_times[selected_date]
            self.comboBoxGio.addItems(available_times)

            if selected_time in available_times:
                self.comboBoxGio.setCurrentText(selected_time)
            else:
                self.comboBoxGio.addItem(f"{selected_time} (Hết chỗ)")
                self.comboBoxGio.setCurrentIndex(self.comboBoxGio.findText(f"{selected_time} (Hết chỗ)"))
        else:
            QMessageBox.warning(self.MainWindow, "Lỗi", f"Giờ {selected_time} không có trong danh sách!")

        # Cập nhật comboBox dịch vụ
        self.comboBoxDichVu.clear()
        for dichvu in self.list_services:
            self.comboBoxDichVu.addItem(dichvu.dichvu)

        # Xác định index của dịch vụ đã chọn
        index_dichvu = self.comboBoxDichVu.findText(info_customer.dichvu)
        if index_dichvu != -1:
            self.comboBoxDichVu.setCurrentIndex(index_dichvu)


        # Chọn RadioButton theo tình trạng
        if info_customer.tinhtrang == "Chưa Xác Nhận":
            self.radioButtonChuaXacNhan.setChecked(True)
        elif info_customer.tinhtrang == "Đã Xác Nhận":
            self.radioButtonDaXacNhan.setChecked(True)
        elif info_customer.tinhtrang == "Đã Khám":
            self.radioButtonDaKham.setChecked(True)

        # Kiểm tra nơi khám (Phòng khám hoặc Khám tại nhà)
        if info_customer.noikham == "Phòng Khám":
            self.radioButtonPhongKham.setChecked(True)
        elif info_customer.noikham == "Khám Tại Gia":
            self.radioButtonKhamTaiGia.setChecked(True)


    def update_comboBox_NgayHen(self):
        self.comboBoxNgayHen.clear()
        self.comboBoxNgayHen.addItems(self.list_dates)
        self.comboBoxNgayHen.setCurrentIndex(-1)  # Không chọn mặc định

        self.comboBoxGio.clear()  # Ban đầu để trống, chờ cập nhật khi chọn ngày

    def update_gio_kham(self):
        selected_date = self.comboBoxNgayHen.currentText()  # Lấy ngày được chọn
        self.comboBoxGio.clear()

        if selected_date in self.list_times:
            self.comboBoxGio.addItems(self.list_times[selected_date])
            self.comboBoxGio.setCurrentIndex(-1)  # Không chọn mặc định

    def update_sdtbacsi(self):
        selected_bacsi = self.comboBoxBacSi.currentText()
        if selected_bacsi in self.doctor_dict:
            self.lineEditsdtbacsi.setText(self.doctor_dict[selected_bacsi])  # Cập nhật SĐT
        else:
            self.lineEditsdtbacsi.clear()

    def search_info(self):
        infor = self.lineEditTimKiem.text().strip().lower()  # Lấy nội dung tìm kiếm và chuyển về chữ thường
        if not infor:
            QMessageBox.warning(self.MainWindow, "Cảnh báo", "Vui lòng nhập dữ liệu vào thanh tìm kiếm!")
            return

        found_any = False  # Cờ kiểm tra có tìm thấy kết quả hay không

        for row in range(self.tableWidgetThongTinLH.rowCount()):
            match_found = False

            for col in range(self.tableWidgetThongTinLH.columnCount()):
                item = self.tableWidgetThongTinLH.item(row, col)
                if item and infor in item.text().strip().lower():
                    match_found = True
                    found_any = True
                    break

            self.tableWidgetThongTinLH.setRowHidden(row, not match_found)

        if not found_any:
            QMessageBox.information(self.MainWindow, "Kết quả", "Không tìm thấy kết quả phù hợp.")

    def search_info_dk(self):
        infor = self.lineEditTimKiemDK.text().strip().lower()  # Lấy nội dung tìm kiếm và chuyển về chữ thường
        if not infor:
            QMessageBox.warning(self.MainWindow, "Cảnh báo", "Vui lòng nhập dữ liệu vào thanh tìm kiếm!")
            return

        found_any = False  # Cờ kiểm tra có tìm thấy kết quả hay không

        for row in range(self.tableWidgetThongTinDK.rowCount()):
            match_found = False

            for col in range(self.tableWidgetThongTinDK.columnCount()):
                item = self.tableWidgetThongTinDK.item(row, col)
                if item and infor in item.text().strip().lower():
                    match_found = True
                    found_any = True
                    break

            self.tableWidgetThongTinDK.setRowHidden(row, not match_found)

        if not found_any:
            QMessageBox.information(self.MainWindow, "Kết quả", "Không tìm thấy kết quả phù hợp.")

    def save_change(self):
        check_CXN = all(
            self.tableWidgetThongTinLH.item(row, 7) and
            self.tableWidgetThongTinLH.item(row, 7).text() == "Chưa Xác Nhận"
            for row in range(self.tableWidgetThongTinLH.rowCount())
        )
        check_DXN = all(
            self.tableWidgetThongTinLH.item(row, 7) and
            self.tableWidgetThongTinLH.item(row, 7).text() == "Đã Xác Nhận"
            for row in range(self.tableWidgetThongTinLH.rowCount())
        )
        # Xác định current_data dựa vào trạng thái của cột thứ 7
        if check_CXN:
            current_data = "Chưa Xác Nhận"
        elif check_DXN:
            current_data = "Đã Xác Nhận"
        else:
            current_data = None
        index = self.tableWidgetThongTinLH.currentRow()
        if index < 0:
            QMessageBox.warning(self.MainWindow, "Lỗi", "Vui lòng chọn một lịch hẹn để cập nhật!")
            return

        madon_item = self.tableWidgetThongTinLH.item(index, 0)
        if not madon_item:
            QMessageBox.warning(self.MainWindow, "Lỗi", "Không tìm thấy mã đơn trong bảng!")
            return

        madon = madon_item.text().strip()
        info_customer = next((info for info in self.info_customer if info.madon == madon), None)

        if not info_customer:
            QMessageBox.warning(self.MainWindow, "Lỗi", f"Không tìm thấy thông tin khách hàng với mã đơn {madon}!")
            return

        if info_customer.tinhtrang == "Đã Khám":
            QMessageBox.warning(self.MainWindow, "Thông báo", 'Lịch hẹn "Đã khám" không thể chỉnh sửa!')
            return

        noi_kham = self.radioButtonKhamTaiGia
        dia_chi = self.lineEditDiaChi.text()
        if noi_kham.isChecked() and (not dia_chi or dia_chi == "Số 86, khu phố 6, phường Linh Xuân, TP Thủ Đức"):
            QMessageBox.warning(
                self.MainWindow,
                "Cảnh báo",
                "Bạn đã chọn 'Khám tại gia', vui lòng nhập địa chỉ hợp lệ!"
            )
            return

        dich_vu=self.comboBoxDichVu.currentText()
        thong_tin=self.lineEditThongTin.text().strip()
        if dich_vu=="Đăng ký nhiều dịch vụ" and (not thong_tin):
            QMessageBox.warning(self.MainWindow, "Cảnh báo","Bạn đã chọn 'Khám nhiều dịch vụ, vui lòng điền các dịch vụ muốn sử dụng!")
            return

        reply = QMessageBox.question(
        self.MainWindow,
        "Xác nhận thay đổi",
        f"Xác nhận thay đổi lịch hẹn của {info_customer.hovaten}?",
        QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
        QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.No:
            return

        info_customer.hovaten = self.lineEditKhachHang.text().strip()
        info_customer.sdt = self.lineEditSoDienThoaiKH.text().strip()
        info_customer.diachi = self.lineEditDiaChi.text().strip()
        info_customer.thongtin = self.lineEditThongTin.text().strip() or "None"
        info_customer.bacsi = self.comboBoxBacSi.currentText()
        info_customer.sdtbacsi = self.lineEditsdtbacsi.text().strip()
        info_customer.ngaykham = self.comboBoxNgayHen.currentText()
        info_customer.giokham = self.comboBoxGio.currentText()
        info_customer.dichvu = self.comboBoxDichVu.currentText()
        info_customer.noikham = "Phòng Khám" if self.radioButtonPhongKham.isChecked() else "Khám Tại Gia"

        tinhtrang_moi = None
        if self.radioButtonChuaXacNhan.isChecked():
            tinhtrang_moi = "Chưa Xác Nhận"
        elif self.radioButtonDaXacNhan.isChecked():
            tinhtrang_moi = "Đã Xác Nhận"
        elif self.radioButtonDaKham.isChecked():
            tinhtrang_moi = "Đã Khám"

            if tinhtrang_moi == "Đã Khám" and not info_customer.bacsi:
                QMessageBox.warning(self.MainWindow, "Lưu ý",
                                        "Cần chọn bác sĩ trước khi chuyển trạng thái sang 'Đã Khám'!")
                return
        info_customer.tinhtrang = tinhtrang_moi
        self.dc.save_update_lich_hen(info_customer)
        self.update_ui(current_data)

        self.hien_thi_lich_hen(self.tableWidgetThongTinDK, tinhtrang_filter=["Đã Khám"])

        QMessageBox.information(self.MainWindow, "Thành công", "Cập nhật thông tin thành công!")


    def delete_appointment(self):
        check_CXN = all(
            self.tableWidgetThongTinLH.item(row, 7) and
            self.tableWidgetThongTinLH.item(row, 7).text() == "Chưa Xác Nhận"
            for row in range(self.tableWidgetThongTinLH.rowCount())
        )
        check_DXN = all(
            self.tableWidgetThongTinLH.item(row, 7) and
            self.tableWidgetThongTinLH.item(row, 7).text() == "Đã Xác Nhận"
            for row in range(self.tableWidgetThongTinLH.rowCount())
        )
        # Xác định current_data dựa vào trạng thái của cột thứ 7
        if check_CXN:
            current_data = "Chưa Xác Nhận"
        elif check_DXN:
            current_data = "Đã Xác Nhận"
        else:
            current_data = None
        index = self.tableWidgetThongTinLH.currentRow()
        if index < 0:
            QMessageBox.warning(self.MainWindow, "Lỗi", "Vui lòng chọn một lịch hẹn để xóa!")
            return

        madon_item = self.tableWidgetThongTinLH.item(index, 0)  # Cột 0 là mã đơn
        if not madon_item:
            QMessageBox.warning(self.MainWindow, "Lỗi", "Không tìm thấy mã đơn trong bảng!")
            return

        madon = madon_item.text().strip()
        info_customer = next((info for info in self.info_customer if info.madon == madon), None)

        if not info_customer:
            QMessageBox.warning(self.MainWindow, "Lỗi", f"Không tìm thấy thông tin khách hàng với mã đơn {madon}!")
            return

        if info_customer.tinhtrang == "Đã Khám":
            QMessageBox.warning(self.MainWindow, "Thông báo", 'Lịch hẹn "Đã Khám" không thể xóa!')
            return

        reply = QMessageBox.question(
            self.MainWindow,
            "Xác nhận xóa",
            f"Xác nhận xóa lịch hẹn của {info_customer.hovaten}?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.No:
            return

        if reply == QMessageBox.StandardButton.Yes:
            self.dc.remove_lich_hen(madon)
            self.info_customer = [info for info in self.info_customer if info.madon != madon]
            self.update_ui(current_data)
            QMessageBox.information(self.MainWindow, "Thành công", "Xóa lịch hẹn thành công!")

    def open_DatHen_window(self):
        self.mainwindow = QMainWindow()
        self.myui = DatHenExt()
        self.myui.setupUi(self.mainwindow)
        self.myui.showWindow()

    def export_to_excel(self):
        # Mở hộp thoại chọn dữ liệu
        dialog = ExportDialog()
        if dialog.exec():  # Nếu người dùng nhấn "Xuất Excel"
            selected_fields = dialog.get_selected_fields()

            if not selected_fields:
                QMessageBox.warning(self.MainWindow, "Thông báo", "Vui lòng chọn ít nhất một trường để xuất.")
                return

            # Đọc dữ liệu từ file JSON
            try:
                with open("../Dataset/Info_Customer.json", "r", encoding="utf-8") as file:
                    customers = json.load(file)
            except Exception as e:
                QMessageBox.critical(self.MainWindow, "Lỗi", f"Lỗi khi đọc dữ liệu: {str(e)}")
                return

            # Kiểm tra dữ liệu đọc được
            if not isinstance(customers, list):
                QMessageBox.critical(self.MainWindow, "Lỗi", "Dữ liệu trong file không hợp lệ!")
                return

            # Xuất dữ liệu ra file Excel
            filename = "../Dataset/xuat_infor_customers.xlsx"
            export_tool = ExportTool()
            export_tool.export_customer_data_to_excel(filename, customers, selected_fields)

            QMessageBox.information(self.MainWindow, "Thành công",
                                    f"Xuất Excel thành công: {', '.join(selected_fields)}")
    def sign_out(self):
        reply = QMessageBox.question(
            self.MainWindow,
            "Xác nhận đăng xuất",
            "Bạn có chắc chắn muốn đăng xuất?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            self.MainWindow.close()  # Đóng cửa sổ hiện tại
            self.mainwindow = QMainWindow()
            self.myui = biaExt()
            self.myui.setupUi(self.mainwindow)
            self.myui.showWindow()

    #dashboard
    def dashboard_khachhang(self):
        try:
            filename="../Dataset/Info_Customer.json"
            with open(filename, "r", encoding="utf-8") as file:
                data = json.load(file)
                so_luong_khach = len(data)  # Đếm số lượng khách hàng
                self.labelSoLieu1.setText(str(so_luong_khach))
        except Exception as e:
            print(f"Lỗi khi đọc file JSON: {e}")
    def dashboard_LH_homnay(self):
        try:
            ngay_hom_nay = datetime.now().strftime("%d/%m/%Y")
            filename="../Dataset/Date_Time.json"
            with open(filename, "r", encoding="utf-8") as file:
                data = json.load(file)


            today = datetime.today().strftime("%d/%m/%Y")
            yesterday = (datetime.today() - timedelta(days=1)).strftime("%d/%m/%Y")

            lh_today = sum(entry["slot_moi"] for entry in data if entry["ngaykham"] == today)
            lh_yesterday = sum(entry["slot_moi"] for entry in data if entry["ngaykham"] == yesterday)

            self.labelSoLieu2.setText(str(lh_today))
            self.updateTag(self.labelTag2, lh_today, lh_yesterday)

        except json.JSONDecodeError:
            print("Lỗi: Không thể đọc file JSON. Kiểm tra lại nội dung file.")
        except Exception as e:
            print(f"Lỗi khi đọc file JSON: {e}")

    def dashboard_LH_tuan(self):
        try:
            filename = "../Dataset/Date_Time.json"
            with open(filename, "r", encoding="utf-8") as file:
                data = json.load(file)

            today = datetime.today()
            start_week = today - timedelta(days=today.weekday())  # Thứ 2 của tuần này
            end_week = start_week + timedelta(days=6)  # Chủ nhật của tuần này

            start_last_week = start_week - timedelta(days=7)
            end_last_week = end_week - timedelta(days=7)

            lh_this_week = sum(entry["slot_moi"] for entry in data if
                               start_week.strftime("%d/%m/%Y") <= entry["ngaykham"] <= end_week.strftime("%d/%m/%Y"))
            lh_last_week = sum(entry["slot_moi"] for entry in data if
                               start_last_week.strftime("%d/%m/%Y") <= entry["ngaykham"] <= end_last_week.strftime(
                                   "%d/%m/%Y"))

            self.labelSoLieu3.setText(str(lh_this_week))
            self.updateTag(self.labelTag3, lh_this_week, lh_last_week)

        except Exception as e:
            print(f"Lỗi khi đọc file JSON: {e}")

    def updateTag(self, label, current, previous):
        if previous == 0:
            percent_change = "N/A"
        else:
            percent_change = ((current - previous) / previous) * 100
            percent_change = f"{percent_change:+.1f}%"
        label.setText(percent_change)

    def bieudoduong(self):
        # Đọc dữ liệu từ Date_Time.json
        filename = "../Dataset/Date_Time.json"
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)

        # Khởi tạo dữ liệu theo thứ
        week_data = {"Monday": 0, "Tuesday": 0, "Wednesday": 0, "Thursday": 0,
                     "Friday": 0, "Saturday": 0, "Sunday": 0}

        # Xử lý dữ liệu
        for item in data:
            ngaykham = item.get("ngaykham", "")
            slot_moi = item.get("slot_moi", 0)

            try:
                date_obj = datetime.strptime(ngaykham, "%d/%m/%Y")
                day_name = date_obj.strftime("%A")
                if day_name in week_data:
                    week_data[day_name] += slot_moi
            except ValueError:
                continue
        # Chuyển đổi dữ liệu để vẽ
        thu_list = list(week_data.keys())
        slot_list = list(week_data.values())

        # Xóa widget cũ nếu có
        if self.labelBieuDo.layout() is None:
            self.labelBieuDo.setLayout(QVBoxLayout())
        else:
            for i in reversed(range(self.labelBieuDo.layout().count())):
                self.labelBieuDo.layout().itemAt(i).widget().setParent(None)

        # Vẽ biểu đồ
        fig, ax = plt.subplots(figsize=(5, 3))
        line, = ax.plot(thu_list, slot_list, marker='o', linestyle='-', color='#4C72B0', linewidth=2)

        #ax.set_title("Xu hướng đặt lịch theo thứ", fontsize=12, fontweight='bold')
        ax.set_xlabel("Thứ trong tuần", fontsize=10)
        ax.set_ylabel("Số lượng đặt", fontsize=10)
        ax.grid(True, linestyle='--', alpha=0.6)

        # Thêm annotation (chú thích) ẩn ban đầu
        annot = ax.annotate("", xy=(0, 0), xytext=(10, 10), textcoords="offset points",
                            bbox=dict(boxstyle="round,pad=0.3", fc="yellow", alpha=0.8),
                            arrowprops=dict(arrowstyle="->", color="black"))
        annot.set_visible(False)

        # Hàm xử lý khi bấm vào điểm trên biểu đồ
        def on_click(event):
            if event.inaxes == ax:
                # Tìm điểm gần nhất
                xdata, ydata = line.get_xdata(), line.get_ydata()
                for i in range(len(xdata)):
                    if abs(event.xdata - i) < 0.3:  # Kiểm tra xem có bấm gần điểm không
                        annot.set_text(f"{slot_list[i]} đơn")
                        annot.xy = (i, ydata[i])
                        annot.set_visible(True)
                        fig.canvas.draw_idle()
                        return
                annot.set_visible(False)
                fig.canvas.draw_idle()

        fig.canvas.mpl_connect("button_press_event",on_click)

        # Hiển thị biểu đồ trong labelBieuDo
        canvas = FigureCanvas(fig)
        self.labelBieuDo.layout().addWidget(canvas)

    def bieudotron(self):
        # Đọc dữ liệu từ Info_Customer.json
        filename = "../Dataset/Info_Customer.json"
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)

        # Đếm số lần đặt lịch của từng khách hàng dựa vào số điện thoại (sdt)
        booking_count = {}
        for item in data:
            sdt = item.get("sdt", "")
            if sdt:
                booking_count[sdt] = booking_count.get(sdt, 0) + 1

        # Phân loại khách hàng
        khach_moi = sum(1 for count in booking_count.values() if count == 1)
        khach_quay_lai = sum(1 for count in booking_count.values() if count > 1)

        # Xóa widget cũ nếu có
        if self.labelBDTron.layout() is None:
            self.labelBDTron.setLayout(QVBoxLayout())
        else:
            for i in reversed(range(self.labelBDTron.layout().count())):
                self.labelBDTron.layout().itemAt(i).widget().setParent(None)

        # Vẽ biểu đồ tròn
        fig, ax = plt.subplots(figsize=(4, 4))
        labels = ["", ""]
        sizes = [khach_moi, khach_quay_lai]
        colors = ["#6bc8f7", "#fae38c"]

        ax.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90,
               wedgeprops={"edgecolor": "white", "linewidth": 1})

        # Hiển thị biểu đồ trong labelBDTron
        canvas = FigureCanvas(fig)
        self.labelBDTron.layout().addWidget(canvas)
