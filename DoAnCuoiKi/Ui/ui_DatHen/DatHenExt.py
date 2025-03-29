import re
from PyQt6.QtWidgets import QMessageBox, QMainWindow
from DoAnCuoiKi.Library.DataConnector import DataConnector
from DoAnCuoiKi.Library.JsonFileFactory import JsonFileFactory
from DoAnCuoiKi.Model.Info_customer import Info_customer
from DoAnCuoiKi.Ui.ui_BiaChinh.biaExt import biaExt
from DoAnCuoiKi.Ui.ui_DatHen.DatHen import Ui_MainWindow


class DatHenExt(QMainWindow,Ui_MainWindow):
    def __init__(self,ho_ten="",sdt=""):
        super().__init__()
        self.dc = DataConnector()
        self.list_times = self.dc.get_all_date_time()
        self.list_dates = self.list_times  # Đảm bảo list_dates có giá trị trước setupUi()
        self.list_services = self.dc.get_all_services()
        self.info_customer = self.dc.get_all_customer()
        self.ho_ten = ho_ten
        self.sdt = sdt
        self.setupUi(self)

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.lineEdit_SDT.setText(self.sdt)
        self.lineEdit_HovaTen.setText(self.ho_ten)
        self.show_times_dates()
        self.show_services()
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()
    def setupSignalAndSlot(self):
        self.pushButton_DatHen.clicked.connect(self.process_appointment)
        self.pushButton_caution.clicked.connect(self.back)
    def show_times_dates(self):
        self.comboBox_NgayKham.clear()
        available_dates = [dt.ngaykham for dt in self.list_dates]
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
    def show_services(self):
        self.comboBox_DichVuKham.clear()
        for dichvu in self.list_services:
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
        if not re.fullmatch(r'0\d{9}', sdt):
            QMessageBox.warning(self.MainWindow, "Cảnh báo","Số điện thoại không hợp lệ! Vui lòng nhập đúng định dạng.")
            return
        if not ngaykham :
            QMessageBox.warning(self.MainWindow, "Cảnh báo", "Vui lòng chọn ngày khám và giờ khám trước khi đặt hẹn")
            return
        if not giokham :
            QMessageBox.warning(self.MainWindow, "Cảnh báo", f"Hiện {ngaykham} đã đầy lịch đặt trước. Vui lòng chọn ngày khám và giờ khám phù hợp")
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
    def back(self):
        self.MainWindow.close()
        self.mainwindow = QMainWindow()
        self.myui = biaExt()
        self.myui.setupUi(self.mainwindow)
        self.myui.showWindow()
