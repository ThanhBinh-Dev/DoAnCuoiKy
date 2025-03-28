
import functools
import hashlib
import os

from PyQt6.QtCore import QTimer
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
        self.json_file = "../Dataset/Info_Customer.json"
        self.last_checked=self.last_info_checked()

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.labelSDT.setText(str(self.sdt))
        self.Show_Name_SDT()
        self.show_info_gui()
        self.show_info_combobox()
        self.setUpSignalandSlots()
        self.timer = QTimer()
        self.timer.timeout.connect(self.check_update)
        self.timer.start(2000)

    def showWindow(self):
        self.MainWindow.show()

    def Show_Name_SDT(self):
        sdt=self.labelSDT.text()
        for info in self.info_customer:
            if str(info.sdt)==str(sdt):
                self.labelHoTen.setText(info.hovaten)
        self.show_info_gui()

    def last_info_checked(self):
        if not os.path.exists(self.json_file):
            return None
        with open(self.json_file, "rb") as f:
            return hashlib.md5(f.read()).hexdigest()

    def check_update(self):
        current_data = self.last_info_checked()
        if current_data and current_data != self.last_checked:
            self.last_checked = current_data  # Cập nhật hash mới nhất
            self.info_customer = self.dckh.get_info_customer()  # Lấy dữ liệu mới
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
        self.clearLayout(self.verticalLayout)# Xóa layout trước khi thêm mới
        self.info_customer=self.dckh.get_info_customer()
        sdt = self.labelSDT.text()
        self.list_info = self.dckh.search_info(sdt)
        self.list_info.sort(key=lambda info: (info.tinhtrang != "Đã Xác Nhận", info.tinhtrang == "Đã Khám"))
        for info in self.list_info:
            text_button = f"{info.ngaykham}\n{info.giokham}\n{info.dichvu}"
            info_button = QPushButton(text_button)
            info_button.setMinimumHeight(70)
            info_button.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;                     \n"
"    background-color: rgb(214, 234, 255);        \n"
"    color: black;\n"
"    border: 1px solid black;\n"
"    text-align: left;\n"
"    padding-left: 5px;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color:rgb(119, 174, 232);\n"
"QPushButton:hover {\n"
"background-color: rgb(119, 174, 232);\n"                                                         
"}\n"
)
            self.verticalLayout.addWidget(info_button)
            info_button.clicked.connect(functools.partial(self.change_color, info_button, info))
    def change_color(self,button,info):
        for i in range(self.verticalLayout.count()):
            widget = self.verticalLayout.itemAt(i).widget()
            if isinstance(widget, QPushButton):
                widget.setStyleSheet("""
                       QPushButton {
                           border-radius: 10px;
                           background-color: rgb(214, 234, 255);
                           color: black;
                           border: 1px solid black;
                           text-align: left;
                           padding-left: 5px;
                       }
                       QPushButton:pressed {
                           background-color: rgb(26, 52, 126);
                           color:white;;
                       }
                        QPushButton:hover {
                           background-color: rgb(119, 174, 232);
                           color:white;
                       }
                   """)

        button.setStyleSheet("""
                       QPushButton {
                           border-radius: 10px;
                           background-color: rgb(119, 174, 232);
                           color: black;
                           border: 1px solid black;
                           text-align: left;
                           padding-left: 5px;
                       }
                       QPushButton:pressed {
                           background-color: rgb(119, 174, 232);
                       }
                       QPushButton:hover {
                           background-color: rgb(119, 174, 232);
                       }
           """)
        self.show_details(info)

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
        self.pushButtonSearch.clicked.connect(self.search_info)
        self.pushButtonreload.clicked.connect(self.reload)

    def Booking(self):
        ho_ten=self.labelHoTen.text().strip()
        sdt=self.labelSDT.text().strip()
        self.mainwindow = QMainWindow()
        self.myui = DatHenExt(ho_ten,sdt)
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

            # Đặt trạng thái "Chưa Xác Nhận" nếu chọn "Khám tại gia"
            if noi_kham == "Khám Tại Gia":
                self.lineEditTinhTrang.setText("Chưa Xác Nhận")  # Sử dụng setText để gán giá trị

                # Kiểm tra địa chỉ hợp lệ
                if not dia_chi or dia_chi == "Số 86, khu phố 6, phường Linh Xuân, TP Thủ Đức":
                    QMessageBox.warning(
                        self.MainWindow,
                        "Cảnh báo",
                        "Bạn đã chọn 'Khám tại gia', vui lòng nhập địa chỉ hợp lệ!"
                    )
                    return
            dich_vu=self.comboBox_DichVu.currentText()
            thong_tin=self.lineEditThongTinThem.text().strip()
            if dich_vu=="Đăng ký nhiều dịch vụ" and (not thong_tin):
                QMessageBox.warning(self.MainWindow, "Cảnh báo","Bạn đã chọn 'Khám nhiều dịch vụ, vui lòng điền các dịch vụ muốn sử dụng!")
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
                if info.sdt == self.selected_info.sdt and info.madon == self.selected_info.madon:
                    info.ngaykham = self.lineEditNgayKham.text()
                    info.giokham = self.lineEditGioKham.text()
                    info.tinhtrang = self.lineEditTinhTrang.text()
                    info.diachi=self.lineEditDiaChi.text()
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

    def search_info(self):
        search = self.lineEditTimKiem.text().strip()
        if not search:
            QMessageBox.warning(self.MainWindow, "Cảnh báo", "Vui lòng nhập ngày khám theo định dạng đ/mm/yyyy"
                                                             "hoặc tên dịch vụ để tìm kiếm!")
            return
        self.clearLayout(self.verticalLayout)
        self.list_info = [info for info in self.info_customer
            if str(search)==str(info.ngaykham.lower())  or str(search.lower()) in str(info.dichvu.lower())
        ]
        self.list_info.sort(key=lambda info: (info.tinhtrang != "Đã Xác Nhận", info.tinhtrang == "Đã Khám"))
        if not self.list_info:
            QMessageBox.information(self.MainWindow, "Thông báo",
                                    "Không tìm thấy kết quả phù hợp.",
                                    "Vui lòng nhập ngày khám theo định dạng đ/mm/yyyy"
                                    "hoặc tên dịch vụ để tìm kiếm!"
                                    )
        else:
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
                                          "    background-color:rgb(26, 52, 126);\n"
                                          "}\n"
                                          "QPushButton:hover {\n"
                                          "background-color: rgb(119, 174, 232);\n"
                                          )
                self.verticalLayout.addWidget(info_button)
                info_button.clicked.connect(functools.partial(self.show_details, info))
    def reload(self):
        self.show_info_gui()

# Chưa có hướng dẫn sử dụng
# Nhấn vào đặt hẹn truyền thông tin tên đăng nhập và số điện thoại khi khách hàng

