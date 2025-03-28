from DoAnCuoiKi.Library.JsonFileFactory import JsonFileFactory
from DoAnCuoiKi.Model.Date_Time import Date_Time

list_date_time=[]
list_date_time.append(Date_Time(" "," ",0,0))

for date in ["23/03/2025","24/03/2025","25/03/2025","26/03/2025","27/03/2025","28/03/2025","29/03/2025","30/03/2025","31/03/2025",
             "01/04/2025","02/04/2025", "03/04/2025", "04/04/2025", "05/04/2025", "06/04/2025", "07/04/2025", "08/04/2025",
             "09/04/2025", "10/04/2025", "11/04/2025", "12/04/2025", "13/04/2025", "14/04/2025", "15/04/2025"]:
    list_date_time.append(Date_Time(date, "8:00 - 9:00", 0, 5))
    list_date_time.append(Date_Time(date, "9:00 - 10:00", 2, 5))
    list_date_time.append(Date_Time(date, "10:00 - 11:00", 5, 5))
    list_date_time.append(Date_Time(date, "13:00 - 14:00", 3, 5))
    list_date_time.append(Date_Time(date, "14:00 - 15:00", 3, 5))
    list_date_time.append(Date_Time(date, "15:00 - 16:00", 4, 5))
    list_date_time.append(Date_Time(date, "16:00 - 17:00", 0, 5))
    list_date_time.append(Date_Time(date, "17:00 - 18:00", 2, 5))
    list_date_time.append(Date_Time(date, "18:00 - 19:00", 0, 5))
    list_date_time.append(Date_Time(date, "19:00 - 20:00", 1, 5))
    list_date_time.append(Date_Time(date, "20:00 - 21:00", 3, 5))
    list_date_time.append(Date_Time(date, "21:00 - 22:00", 2, 5))

jff=JsonFileFactory()
filename= "../Dataset/Date_Time.json"
jff.write_data(list_date_time,filename)