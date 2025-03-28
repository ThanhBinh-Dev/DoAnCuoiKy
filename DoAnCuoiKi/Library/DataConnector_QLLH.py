from DoAnCuoiKi.Library.JsonFileFactory import JsonFileFactory


from DoAnCuoiKi.Model.Date_Time import Date_Time
from DoAnCuoiKi.Model.DichVuKham import DichVuKham
from DoAnCuoiKi.Model.Doctor import Doctor
from DoAnCuoiKi.Model.Info_customer import Info_customer


class DataConnector_QLLH:
    def get_info_customer(self):
        jff = JsonFileFactory()
        filename = '../Dataset/Info_Customer.json'
        list_info = jff.read_data(filename, Info_customer)
        return list_info

    def get_date_time_data(self):
        jff=JsonFileFactory()
        filename='../Dataset/Date_Time.json'
        list_Date_Time=jff.read_data(filename,Date_Time)
        return  list_Date_Time

    def get_all_services(self):
        jff = JsonFileFactory()
        filename = "../Dataset/DichVuKham.json"
        list_services = jff.read_data(filename, DichVuKham)
        return list_services

    def get_all_doctor(self):
        jff = JsonFileFactory()
        filename = "../Dataset/Doctor.json"
        list_doctor = jff.read_data(filename, Doctor)
        return list_doctor

    def sort_info_customer(self):
        self.info_customer = self.get_info_customer()

        def sort_key(info_customer):
            return (info_customer.ngaykham, info_customer.giokham)

        self.info_customer.sort(key=sort_key)
        return self.info_customer


    def sort_gio_kham_con_slot_trong_ngay(self, ngaykham):
        list_Date_Time = self.get_date_time_data()
        # Lọc danh sách: chỉ lấy những giờ khám có slot_moi khác 0 trong ngày được chỉ định
        list_gio_kham = [dt.giokham for dt in list_Date_Time if dt.ngaykham == ngaykham and dt.slot_moi != 0]
        return list_gio_kham

    def sort_ngay_kham_con_slot(self):
        list_Date_Time = self.get_date_time_data()
        unique_dates = set(dt.ngaykham for dt in list_Date_Time)
        list_ngay_con_slot = [ngay for ngay in unique_dates if self.sort_gio_kham_con_slot_trong_ngay(ngay)]
        return list_ngay_con_slot

    def find_index_lich_hen(self, madon):
        self.info_customer = self.get_info_customer()
        for i in range(len(self.info_customer)):
            customer = self.info_customer[i]
            if customer.madon == madon :
                return i
        return -1


    def save_update_lich_hen(self, current_customer):
        index = self.find_index_lich_hen(current_customer.madon)
        if index != -1:
            self.info_customer[index] = current_customer
            jff = JsonFileFactory()
            filename = "../Dataset/Info_Customer.json"
            jff.write_data(self.info_customer, filename)


    def remove_lich_hen(self, madon):
        index = self.find_index_lich_hen(madon)
        if index != -1:
            self.info_customer.pop(index)

            jff = JsonFileFactory()
            filename = "../Dataset/Info_Customer.json"
            jff.write_data(self.info_customer, filename)





