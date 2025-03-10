from DoAnCuoiKi.Library.JsonFileFactory import JsonFileFactory
from DoAnCuoiKi.Model.Time import Time
list_times=[]
jff=JsonFileFactory()
filename="../Dataset/Time.json"
list_times=jff.read_data(filename,Time)
for time in list_times:
    print(time)