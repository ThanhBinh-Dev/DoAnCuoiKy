from DoAnCuoiKi.Library.JsonFileFactory import JsonFileFactory
from DoAnCuoiKi.Model.Doctor import Doctor

list_doctors=[]
list_doctors.append(Doctor("Nguyễn Văn An", "0912345678"))
list_doctors.append(Doctor("Trần Thị Bích", "0987654321"))
list_doctors.append(Doctor("Phạm Quang Huy", "0909888776"))
list_doctors.append(Doctor("Lê Minh Châu", "0933445566"))
list_doctors.append(Doctor("Đỗ Thị Lan", "0977556677"))
list_doctors.append(Doctor("Vũ Văn Nam", "0911223344"))
list_doctors.append(Doctor("Trịnh Thị Hạnh", "0988112233"))
list_doctors.append(Doctor("Lý Thị Xuân", "0935667788"))

jff=JsonFileFactory()
filename= "../Dataset/Doctor.json"
jff.write_data(list_doctors,filename)