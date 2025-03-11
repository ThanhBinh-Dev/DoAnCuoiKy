from DoAnCuoiKi.Library.JsonFileFactory import JsonFileFactory
from DoAnCuoiKi.Model.Date import Date
from DoAnCuoiKi.Model.Date_Time import Date_Time
from DoAnCuoiKi.Model.Time import Time

list_times=[]
jff=JsonFileFactory()
filename="../Dataset/Date_Time.json"
list_times=jff.read_data(filename,Date_Time)
for time in list_times:
    print(time)