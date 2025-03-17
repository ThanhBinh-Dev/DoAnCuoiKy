import re

from PyQt6.QtWidgets import QMessageBox,QMainWindow
from PyQt6.uic.Compiler.qtproxies import QtWidgets

from DoAnCuoiKi.Library.DataConnector import DataConnector
from DoAnCuoiKi.Library.JsonFileFactory import JsonFileFactory
from DoAnCuoiKi.Model.Info_customer import Info_customer
from DoAnCuoiKi.Ui.ui_DatHen.DatHen import Ui_MainWindow


class DatHenExt(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.dc = DataConnector()
        self.list_times = self.dc.get_all_date_time()
        self.list_dates = self.list_times  # Đảm bảo list_dates có giá trị trước setupUi()
        self.list_serviecs = self.dc.get_all_servieces()
        self.info_customer = self.dc.get_all_customer()
        self.setupUi(self)  # Gọi setupUi sau khi khởi tạo biến

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.show_times_dates()
        self.show_serviecs()
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()
    def setupSignalAndSlot(self):
        self.pushButton_DatHen.clicked.connect(self.process_appointment)
    def show_times_dates(self):
        self.comboBox_NgayKham.clear()
        available_dates = [dt.ngaykham for dt in self.list_dates if dt.slot_moi < dt.slot_gioihan]
        available_dates=list(set(available_dates))
        available_dates.sort()
        self.comboBox_NgayKham.addItems(available_dates)
        self.comboBox_NgayKham.currentTextChanged.connect(self.update_times)
        if available_dates:
            self.update_times()
    def update_times(self):
        selected_date=self.comboBox_NgayKham.currentText()
        self.comboBox_GioKham.clear()
        available_times = [dt.giokham for dt in self.list_times if (dt.slot_moi < dt.slot_gioihan) and (dt.ngaykham==selected_date)]
        self.comboBox_GioKham.addItems(available_times)
    def show_serviecs(self):
        self.comboBox_DichVuKham.clear()
        for dichvu in self.list_serviecs:
            self.comboBox_DichVuKham.addItem(dichvu.dichvu)
    def process_appointment(self):
        # Ghi File
        hovaten=self.lineEdit_HovaTen.text().strip()
        sdt=self.lineEdit_SDT.text().strip()
        diachi=self.lineEdit_DiaChi.text().strip()
        ngaykham=self.comboBox_NgayKham.currentText()
        giokham=self.comboBox_GioKham.currentText()
        dichvu=self.comboBox_DichVuKham.currentText()
        thongtin=self.lineEdit_ThongTinThem.text().strip()
        if not hovaten:
            QMessageBox.warning(self.MainWindow, "Cảnh báo", "Vui lòng nhập Họ và Tên")
            return
        if not re.fullmatch(r'\d{10}', sdt):
            QMessageBox.warning(self.MainWindow, "Cảnh báo","Số điện thoại không hợp lệ! Vui lòng nhập đúng định dạng.")
            return
        if self.radioButton_PhongKham.isChecked():
            noikham = "Phòng Khám"
            if not diachi:
                diachi = "Số 86, khu phố 6, phường Linh Xuân, TP Thủ Đức"
        elif self.radioButton_KhamTaiGia.isChecked():
            noikham = "Khám Tại Gia"
            if not diachi:
                QMessageBox.warning(self.MainWindow, "Cảnh báo", "Vui lòng nhập địa chỉ khi khám tại gia")
                return
        else:
            QMessageBox.warning(self.MainWindow, "Cảnh báo", "Vui lòng chọn nơi khám")
            return
        if not thongtin:
            thongtin="None"
        jff = JsonFileFactory()
        filename = "../Dataset/Info_Customer.json"
        current_data = jff.read_data(filename, Info_customer)
        current_data = [Info_customer(**data) if isinstance(data, dict) else data for data in current_data]
        new_customer = Info_customer(hovaten,sdt, noikham, diachi, ngaykham, giokham, dichvu, thongtin)
        self.info_customer.append(new_customer)
        current_data.insert(0, new_customer)
        jff.write_data(current_data, filename)
        self.dc.calculate_slot(ngaykham,giokham)
        #Ghi Slot Đặt Hẹn Mới
        self.list_times = self.dc.get_all_date_time()
        self.list_dates = self.list_times
        self.show_times_dates()
        QMessageBox.information(self.MainWindow, "Thành công", "Đặt hẹn thành công!")

        from DoAnCuoiKi.Ui.ui_PhieuXacNhan.PhieuXacNhanExt import PhieuXacNhanExt # Import muộn để tránh vòng lặp
        self.phieu_xac_nhan_window = PhieuXacNhanExt()
        self.phieu_xac_nhan_window.show()
        self.MainWindow.close()# Đóng giao diện đặt hẹn trước khi mở giao diện mới