from DoAnCuoiKi.Library.JsonFileFactory import JsonFileFactory
from DoAnCuoiKi.Model.Time import Time

list_time=[]
list_time.append(Time("8:00 - 9:00"))
list_time.append(Time("9:00 - 10:00"))
list_time.append(Time("10:00 - 11:00"))
list_time.append(Time("13:00 - 14:00"))
list_time.append(Time("14:00 - 15:00"))
list_time.append(Time("15:00 - 16:00"))
list_time.append(Time("16:00 - 17:00"))
jff=JsonFileFactory()
filename="../Dataset/Time.json"
jff.write_data(list_time,filename)