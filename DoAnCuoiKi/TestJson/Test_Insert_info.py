from DoAnCuoiKi.Library.Data_Connector_QLKH import DataConnector_QLKH

info_customer = []
dckh=DataConnector_QLKH()
list_info = dckh.search_info('0976854923')

# In danh sách để kiểm tra
for i in list_info:
    print(i)

