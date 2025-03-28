import json
from datetime import datetime, timedelta

from PyQt6.QtWidgets import QHeaderView

from DoAnCuoiKi.Ui.ui_QuanLyLichHen.QuanLyLichHen import Ui_MainWindow


class QLLHExt(Ui_MainWindow):
    def __init__(self):
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
        self.actionQuayLai.triggered.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.actionThongKe.triggered.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.thongke_khachhang()
        self.thongke_LH_homnay()
        self.thongke_LH_tuan()
    def showWindow(self):
        self.MainWindow.show()
    def thongke_khachhang(self):
        try:
            filename="../Dataset/Info_Customer.json"
            with open(filename, "r", encoding="utf-8") as file:
                data = json.load(file)
                so_luong_khach = len(data)  # Đếm số lượng khách hàng
                self.labelSoLieu1.setText(str(so_luong_khach))
        except Exception as e:
            print(f"Lỗi khi đọc file JSON: {e}")
    def thongke_LH_homnay(self):
        try:
            ngay_hom_nay = datetime.now().strftime("%d/%m/%Y")
            filename="../Dataset/Date_Time.json"
            with open(filename, "r", encoding="utf-8") as file:
                data = json.load(file)  # Đọc file JSON


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

    def thongke_LH_tuan(self):
        try:
            filename = "../Dataset/Date_Time.json"
            with open(filename, "r", encoding="utf-8") as file:
                data = json.load(file)  # Đọc file JSON

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