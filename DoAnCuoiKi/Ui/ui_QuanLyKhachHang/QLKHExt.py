import functools

from PyQt6.QtWidgets import QPushButton, QMainWindow, QMessageBox

from DoAnCuoiKi.Library.DataConnector import DataConnector
from DoAnCuoiKi.Library.Data_Connector_QLKH import DataConnector_QLKH
from DoAnCuoiKi.Library.JsonFileFactory import JsonFileFactory
from DoAnCuoiKi.Ui.ui_BiaChinh.biaExt import biaExt
from DoAnCuoiKi.Ui.ui_DatHen.DatHenExt import DatHenExt
from DoAnCuoiKi.Ui.ui_QuanLyKhachHang.QLKH import Ui_MainWindow
from DoAnCuoiKi.Ui.ui_QuanLyKhachHang.qrExt import QrExt


class QLKHExt(Ui_MainWindow):
    def __init__(self,sdt="None"):
        self.dckh = DataConnector_QLKH()
        self.dc=DataConnector()
        self.list_serviecs=self.dc.get_all_servieces()
        self.list_info=[]
        self.info_customer=self.dckh.get_info_customer()
        self.jff = JsonFileFactory()
        self.selected_info=None
        self.sdt=sdt
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.labelSDT.setText(str(self.sdt))
        self.Show_Name_SDT()
        self.show_info_gui()
        self.show_info_combobox()
        self.setUpSignalandSlots()
    def showWindow(self):
        self.MainWindow.show()
    def Show_Name_SDT(self):
        sdt=self.labelSDT.text()
        for info in self.info_customer:
            if str(info.sdt)==str(sdt):
                self.labelHoTen.setText(info.hovaten)
        self.show_info_gui()
    def clearLayout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.clearLayout(item.layout())

    def show_info_gui(self):
        self.clearLayout(self.verticalLayout)
        self.info_customer=self.dckh.get_info_customer()# Xóa layout trước khi thêm mới
        sdt = self.labelSDT.text()
        self.list_info = self.dckh.search_info(sdt)
        for info in self.list_info:
            text_button = f"{info.ngaykham}\n{info.giokham}\n{info.dichvu}"
            info_button = QPushButton(text_button)
            info_button.setMinimumHeight(70)
            info_button.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;                     \n"
"    background-color: rgb(214,234,255);        \n"
"    color: black;\n"
"    border: 1px solid black;\n"
"    text-align: left;\n"
"    padding-left: 5px;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color:rgb(119, 174, 232);\n"
"}\n"
)
            self.verticalLayout.addWidget(info_button)
            info_button.clicked.connect(functools.partial(self.show_details, info))
    def show_info_combobox(self):
        self.comboBox_DichVu.clear()
        for dichvu in self.list_serviecs:
            self.comboBox_DichVu.addItem(dichvu.dichvu)
    def show_details(self, info):
        self.selected_info = info
        self.lineEditNgayKham.setText(info.ngaykham)
        self.lineEditGioKham.setText(info.giokham)
        self.lineEditTinhTrang.setText(info.tinhtrang)
        self.lineEditThongTinThem.setText(info.thongtin)
        self.lineEditDiaChi.setText(info.diachi)
        self.comboBox_DichVu.setCurrentText(info.dichvu)
        self.comboBox_NoiKham.setCurrentText(info.noikham)
    def setUpSignalandSlots(self):
        self.pushButtonAdd.clicked.connect(self.Booking)
        self.pushButtonPrint.clicked.connect(self.Open_qr)
        self.pushButtonSave.clicked.connect(self.save_info)
        self.pushButtonDangXuat.clicked.connect(self.SignOut)
    def Booking(self):
        self.mainwindow = QMainWindow()
        self.myui = DatHenExt()
        self.myui.setupUi(self.mainwindow)
        self.myui.showWindow()
    def Open_qr(self):
        self.mainwindow = QMainWindow()
        self.myui = QrExt()
        self.myui.setupUi(self.mainwindow)
        self.myui.showWindow()
    def save_info(self):
        if self.selected_info:
            noi_kham = self.comboBox_NoiKham.currentText()
            dia_chi = self.lineEditDiaChi.text().strip()
            if noi_kham == "Khám tại gia" and (not dia_chi or dia_chi == "Số 86, khu phố 6, phường Linh Xuân, TP Thủ Đức"):
                QMessageBox.warning(self.MainWindow,"Cảnh báo","Bạn đã chọn 'Khám tại gia', vui lòng nhập địa chỉ hợp lệ!")
                return
            dich_vu=self.comboBox_DichVu.currentText()
            thong_tin=self.lineEditThongTinThem.text().strip()
            if dich_vu=="Đăng ký nhiều dịch vụ" and (not thong_tin):
                QMessageBox.warning(self.MainWindow, "Cảnh báo","Bạn đã chọn 'Khám nhiều dịch vụ, vui lòng các dịch vụ muốn sử dụng!")
                return
            if not dich_vu:
                QMessageBox.warning(self.MainWindow, "Cảnh báo","Vui lòng chọn trước dịch vụ")
                return
            reply=QMessageBox.question(
                self.MainWindow,
                "Xác Nhận Thay Đổi",
                "Bạn có chắc chắn muốn thay đổi thông tin lịch hẹn không?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                QMessageBox.StandardButton.No
            )
            if reply == QMessageBox.StandardButton.No:
                return
            filename = "../Dataset/Info_Customer.json"
            list_info = self.jff.read_data(filename, type(self.selected_info))
            for info in list_info:
                if info.sdt == self.selected_info.sdt and info.ngaykham == self.selected_info.ngaykham and info.giokham == self.selected_info.giokham:
                    info.ngaykham = self.lineEditNgayKham.text()
                    info.giokham = self.lineEditGioKham.text()
                    info.tinhtrang = self.lineEditTinhTrang.text()
                    info.thongtin = self.lineEditThongTinThem.text()
                    info.dichvu = self.comboBox_DichVu.currentText()
                    info.noikham = self.comboBox_NoiKham.currentText()
                    break
            self.jff.write_data(list_info, filename)
        self.show_info_gui()
    def SignOut(self):
        self.MainWindow.close()
        self.mainwindow = QMainWindow()
        self.myui = biaExt()
        self.myui.setupUi(self.mainwindow)
        self.myui.showWindow()
# Dữ liệu chưa tự cập nhật hay xuất hiện khi khách hàng thêm lịch mới
# Chưa có hướng dẫn sử dụng
# M nghĩ có cần xóa ngày sau khi các ca trong đó đầy hết rồi không, hay chỉ cần hiện thông báo ngày đó full r thôi
