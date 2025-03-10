from DoAnCuoiKi.Model.Date import Date
from DoAnCuoiKi.Model.DichVuKham import DichVuKham
from DoAnCuoiKi.Model.Time import Time
from Review.Project85.Library.JsonFileFactory import JsonFileFactory


class DataConnector:
    def get_all_time(self):
        list_times=[]
        jff=JsonFileFactory()
        filename="../Dataset/Time.json"
        list_times=jff.read_data(filename,Time)
        return list_times
    def get_all_day(self):
        list_dates=[]
        jff = JsonFileFactory()
        filename = "../Dataset/Date.json"
        list_dates = jff.read_data(filename, Date)
        return list_dates
    def get_all_servieces(self):
        list_servieces=[]
        jff = JsonFileFactory()
        filename = "../Dataset/DichVuKham.json"
        list_servieces = jff.read_data(filename, DichVuKham)
        return list_servieces