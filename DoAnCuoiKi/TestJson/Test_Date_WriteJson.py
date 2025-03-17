from DoAnCuoiKi.Library.JsonFileFactory import JsonFileFactory
from DoAnCuoiKi.Model.Date import Date

list_date=[]
list_date.append(Date("01/04/2025"))
list_date.append(Date("02/04/2025"))
list_date.append(Date("03/04/2025"))
list_date.append(Date("04/04/2025"))
list_date.append(Date("05/04/2025"))
list_date.append(Date("06/04/2025"))
list_date.append(Date("07/04/2025"))
list_date.append(Date("08/04/2025"))
list_date.append(Date("09/04/2025"))
list_date.append(Date("10/04/2025"))

jff=JsonFileFactory()
filename= "../Dataset/Date.json"
jff.write_data(list_date,filename)