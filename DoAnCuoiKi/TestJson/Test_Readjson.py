from DoAnCuoiKi.Library.DataConnector import DataConnector
from DoAnCuoiKi.Library.Data_Connector_QLKH import DataConnector_QLKH

dc=DataConnector()
list=dc.get_all_date_time()
for i in list:
    print(i.ngaykham)