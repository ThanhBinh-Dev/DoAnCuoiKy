from DoAnCuoiKi.Library.JsonFileFactory import JsonFileFactory
from DoAnCuoiKi.Model.Date import Date

list_date=[]
list_date.append(Date("23/03/2025"))
list_date.append(Date("24/03/2025"))
list_date.append(Date("25/03/2025"))
list_date.append(Date("26/03/2025"))
list_date.append(Date("27/03/2025"))
list_date.append(Date("18/04/2025"))
list_date.append(Date("29/04/2025"))
list_date.append(Date("30/04/2025"))
list_date.append(Date("31/03/2025"))
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
list_date.append(Date("11/04/2025"))
list_date.append(Date("12/04/2025"))
list_date.append(Date("13/04/2025"))
list_date.append(Date("14/04/2025"))
list_date.append(Date("15/04/2025"))

jff=JsonFileFactory()
filename= "../Dataset/Date.json"
jff.write_data(list_date,filename)