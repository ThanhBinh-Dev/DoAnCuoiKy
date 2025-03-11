from DoAnCuoiKi.Model.Date import Date
from DoAnCuoiKi.Model.Date_Time import Date_Time
from DoAnCuoiKi.Model.DichVuKham import DichVuKham
from DoAnCuoiKi.Model.Info_customer import Info_customer
from DoAnCuoiKi.Model.Time import Time
from Review.Project85.Library.JsonFileFactory import JsonFileFactory


class DataConnector:
    def get_all_date_time(self):
        list_times=[]
        jff=JsonFileFactory()
        filename="../Dataset/Date_Time.json"
        list_times=jff.read_data(filename,Date_Time)
        return list_times
    def get_all_servieces(self):
        list_servieces=[]
        jff = JsonFileFactory()
        filename = "../Dataset/DichVuKham.json"
        list_servieces = jff.read_data(filename, DichVuKham)
        return list_servieces
    def get_all_customer(self):
        list_customers=[]
        jff = JsonFileFactory()
        filename = "../Dataset/Info_Customer.json"
        list_customers = jff.read_data(filename, Info_customer)
        return list_customers
    def calculate_slot(self,ngaykham,giokham):
        self.list_date_time=self.get_all_date_time()
        for i in range (len(self.list_date_time)):
            date_time = self.list_date_time[i]
            if (date_time.ngaykham==ngaykham) and (date_time.giokham==giokham):
                date_time.slot_moi+=1
                jff = JsonFileFactory()
                filename = "../Dataset/Date_Time.json"
                jff.write_data(self.list_date_time, filename)
                return i

