import json
import os

from DoAnCuoiKi.Library.JsonFileFactory import JsonFileFactory
from DoAnCuoiKi.Model.Admin import Admin
from DoAnCuoiKi.Model.Date_Time import Date_Time
from DoAnCuoiKi.Model.DichVuKham import DichVuKham



class DataConnector:
    def read_json_file(self, file_path):
        """Đọc file JSON và trả về danh sách dữ liệu"""
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                return json.load(file)  # Trả về dạng list[dict]
        except Exception as e:
            print(f"Lỗi khi mở file {file_path}: {e}")
            return []

    def get_all_date_time(self):
        list_times = []
        jff = JsonFileFactory()
        filename = "../Dataset/Date_Time.json"
        list_times = jff.read_data(filename, Date_Time)
        return list_times

    def get_all_servieces(self):
        list_servieces = []
        jff = JsonFileFactory()
        filename = "../Dataset/DichVuKham.json"
        list_servieces = jff.read_data(filename, DichVuKham)
        return list_servieces

    def get_all_customer(self):
        filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../Dataset/Info_Customer.json")
        return self.read_json_file(filename)

    def get_all_admins(self):
        list_admins = []
        jff = JsonFileFactory()
        filename = "../Dataset/Admin.json"
        list_admins = jff.read_data(filename, Admin)
        return list_admins

    # Truy xuất dữ liệu tài khoản đăng nhập
    def login(self, username, password):
        customers = self.get_all_customer()
        for customer in customers:
            if customer["tendangnhap"] == username and customer["matkhau"] == password:
                return "customer"

        admins = self.get_all_admins()
        for admin in admins:
            if admin.tendangnhap == username and admin.matkhau == password:  # Sử dụng thuộc tính thay vì .get()
                return "admin"

        return None

    def get_user_by_phone(self, phone_number):
        try:
            # Xác định đường dẫn file chính xác
            base_path = os.path.dirname(os.path.abspath(__file__))  # Lấy thư mục hiện tại của script
            dataset_path = os.path.join(base_path, "../Dataset")  # Điều chỉnh theo cấu trúc thư mục của bạn

            customers = self.read_json_file(os.path.join(dataset_path, "Info_Customer.json"))
            admins = self.read_json_file(os.path.join(dataset_path, "Admin.json"))

            # Kiểm tra số điện thoại
            for user in customers + admins:
                if user.get("sdt") == phone_number or user.get("sodienthoai") == phone_number:
                    return {"tendangnhap": user["tendangnhap"], "matkhau": user["matkhau"]}

        except Exception as e:
            print(f"Lỗi khi đọc dữ liệu: {e}")

        return None

    def calculate_slot(self, ngaykham, giokham):
        self.list_date_time = self.get_all_date_time()
        for i in range(len(self.list_date_time)):
            date_time = self.list_date_time[i]
            if date_time.ngaykham == ngaykham and date_time.giokham == giokham:
                date_time.slot_moi += 1
                jff = JsonFileFactory()
                filename = "../Dataset/Date_Time.json"
                jff.write_data(self.list_date_time, filename)
                return i
