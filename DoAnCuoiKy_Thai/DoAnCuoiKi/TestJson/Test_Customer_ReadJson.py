from DoAnCuoiKy_Thai.DoAnCuoiKi.Library.JsonFileFactory import JsonFileFactory
from DoAnCuoiKy_Thai.DoAnCuoiKi.Model.Customer import Customer  # Đảm bảo có lớp này
import json

# Khởi tạo JsonFileFactory
jff = JsonFileFactory()
filename = "C:/Users/thain/PycharmProjects/K24406H/DoAnCuoiKy_Thai/DoAnCuoiKi/dataset/Info_Customer.json"


# Kiểm tra nội dung file JSON trước khi đọc
with open(filename, "r", encoding="utf-8") as file:
    raw_data = file.read()
    print("Dữ liệu JSON thô:", raw_data)  # Debug: Kiểm tra dữ liệu JSON

try:
    customers = jff.read_data(filename, Customer)
    print("List of Customers after Loading Json:")
    for customer in customers:
        print(customer)
except json.JSONDecodeError as e:
    print("Lỗi khi parse JSON:", e)
except TypeError as e:
    print("Lỗi TypeError:", e)
