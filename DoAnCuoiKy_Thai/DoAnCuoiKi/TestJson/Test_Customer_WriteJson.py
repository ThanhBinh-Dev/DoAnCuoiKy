from DoAnCuoiKi.Library.JsonFileFactory import JsonFileFactory
from DoAnCuoiKi.Model.Customer import Customer

list_customer=[]

list_customer.append(Customer("Nguyễn Văn An", "0987654321","Khám Tại Gia", "456 Đường Trần Phú, TP HCM","Chó Poodle, 2 tuổi, biếng ăn, nôn nhẹ, có dấu hiệu mệt mỏi, cần kiểm tra tiêu hóa."))
list_customer.append(Customer("Trần Thị Bích", "0912345678","Phòng Khám"))
list_customer.append(Customer("Phạm Quang Huy", "0909988776","Phòng Khám","None","Mèo Anh lông ngắn, 1 tuổi, rụng lông nhiều, gãi liên tục, nghi ngờ dị ứng da."))
list_customer.append(Customer("Lê Minh Châu", "0933445566","Phòng Khám"))
list_customer.append(Customer("Đỗ Thị Lan", "0977556677","Khám Tại Gia","64 Đường Đội Cấn, TP HCM"))
list_customer.append(Customer("Vũ Văn Nam", "0911223344","Phòng Khám"))
list_customer.append(Customer("Trịnh Thị Hạnh", "0988112233","Phòng Khám"))
list_customer.append(Customer("Lý Thị Xuân", "0935667788","Phòng Khám","None","Husky, 3 tuổi, hoạt bát nhưng sụt cân nhanh, cần xét nghiệm tổng quát."))
list_customer.append(Customer("Đặng Quang Minh", "0977111222","Phòng Khám"))
list_customer.append(Customer("Trần Văn Tiến", "0903445566","Phòng Khám"))
list_customer.append(Customer("Hoàng Thị Liên", "0988997766","Khám Tại Gia","88 Đường Nguyễn Huệ, TP HCM","Chihuahua, 5 tháng tuổi, ho khan, chảy nước mũi, nghi ngờ viêm đường hô hấp."))
list_customer.append(Customer("Nguyễn Thị Mai", "0911998855","Phòng Khám"))
list_customer.append(Customer("Lê Quang Phát", "0909223344","Phòng Khám","None","Mèo Sphynx, 2 tuổi, nổi mẩn đỏ trên da, gãi nhiều, nghi ngờ nhiễm nấm."))
list_customer.append(Customer("Phạm Minh Tuấn", "0933998877","Khám Tại Gia","10 Đường Trường Sa, Bình Dương","Mèo Ba Tư, 4 tuổi, ăn ít, mắt chảy dịch, có dấu hiệu sốt nhẹ."))
list_customer.append(Customer("Trịnh Thị Nga", "0977665544","Phòng Khám"))
list_customer.append(Customer("Đinh Văn Dũng", "0901888777","Khám Tại Gia","456 Đường Trần Phú, TP HCM","Golden Retriever, 2 tuổi, lười vận động, sưng khớp chân, cần khám xương khớp."))
list_customer.append(Customer("Nguyễn Thị Hoa", "0911555666","Phòng Khám","None","Pomeranian, 9 tháng tuổi, sợ hãi, run rẩy, có dấu hiệu stress, cần tư vấn tâm lý."))
list_customer.append(Customer("Vũ Minh Khang", "0988333222","Phòng Khám"))
list_customer.append(Customer("Phan Thị Hồng", " 0909777333","Phòng Khám","None","Bulldog, 3 tuổi, thở khò khè, khó chịu khi vận động, cần khám đường hô hấp."))
list_customer.append(Customer("Trần Minh Hiếu", "0977445566","Khám Tại Gia","127 Nguyễn Văn Tăng, TP HCM","Mèo Scottish, 8 tháng tuổi, tiêu chảy nhẹ, bỏ ăn, cần kiểm tra đường ruột."))
list_customer.append(Customer("Nguyễn Thị Hường", "0911667788","Khám Tại Gia", "729 Lê Văn Việt, TP HCM","Mèo Bengal, 3 tuổi, cắn lông liên tục, da đỏ, nghi ngờ viêm da hoặc dị ứng."))
list_customer.append(Customer("Lê Quang Vinh", "0988111224","Phòng Khám"))
list_customer.append(Customer("Trịnh Văn Thịnh", "0909333777","Phòng Khám","None","Mèo Bengal, 3 tuổi, cắn lông liên tục, da đỏ, nghi ngờ viêm da hoặc dị ứng."))
list_customer.append(Customer("Ngô Thị Bích", "0987654321","Phòng Khám","None","Corgi, 1,5 tuổi, tăng cân nhanh, thở gấp, nghi ngờ béo phì, cần tư vấn dinh dưỡng."))
list_customer.append(Customer("Nguyễn Thanh Phong", "0909444555","Phòng Khám"))
list_customer.append(Customer("Trần Ngọc Anh", "0988999988","Khám Tại Gia", "23 Hẻm Linh Hoàng, Hoàng Diệu 2, TP HCM"))
list_customer.append(Customer("Lê Thị Cẩm", "0976328741","Phòng Khám"))

jff=JsonFileFactory()
filename="../Dataset/Customer.json"
jff.write_data(list_customer,filename)