from DoAnCuoiKi.Library.JsonFileFactory import JsonFileFactory
from DoAnCuoiKi.Model.Date import Date
from DoAnCuoiKi.Model.Time import Time

list_dates = []
jff = JsonFileFactory()
filename = "../Dataset/Date.json"
list_dates = jff.read_data(filename, Date)
for time in list_dates:
    print(time)