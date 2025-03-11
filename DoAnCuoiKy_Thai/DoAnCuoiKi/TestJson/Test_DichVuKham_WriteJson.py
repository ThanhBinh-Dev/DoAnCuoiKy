from DoAnCuoiKi.Library.JsonFileFactory import JsonFileFactory
from DoAnCuoiKi.Model.DichVuKham import DichVuKham

dvks=[]
dvks.append(DichVuKham("Khám Tổng Quát"))
dvks.append(DichVuKham("Tiêm Phòng"))
dvks.append(DichVuKham("Tẩy Giun"))
dvks.append(DichVuKham("Siêu Âm"))
dvks.append(DichVuKham("Cắt Tỉa"))
dvks.append(DichVuKham("Tắm"))
dvks.append(DichVuKham("Triệt Sản"))
dvks.append(DichVuKham("Chụp Xquang"))
dvks.append(DichVuKham("Xét Nghiệm"))
dvks.append(DichVuKham("Tư Vấn"))
dvks.append(DichVuKham("Cấy ghép vi mạch nhận dạng"))
jff=JsonFileFactory()
filename="../Dataset/DichVuKham.json"
jff.write_data(dvks,filename)