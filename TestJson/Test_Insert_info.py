from DoAnCuoiKi.Library.JsonFileFactory import JsonFileFactory
from DoAnCuoiKi.Model.Info_customer import Info_customer

info_customer = []
jff = JsonFileFactory()
filename = "../Dataset/Info_Customer.json"
current_data = jff.read_data(filename, Info_customer)
current_data = [Info_customer(**data) if isinstance(data, dict) else data for data in current_data]
new_customer = Info_customer("Nguyễn Thị Bé Ba", "0978236542", "Khám Tại Gia", "Thủ Đức","07/04/2025", "9:00 - 10:00", "Tẩy Giun", "None")
info_customer.append(new_customer)
current_data.insert(0, new_customer)
jff.write_data(current_data, filename)

# In danh sách để kiểm tra
for i in info_customer:
    print(i)

