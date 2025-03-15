from DoAnCuoiKi.Library.DataConnector_KH import DataConnector_QLKH

dc=DataConnector_QLKH()
list_info=dc.get_info_customer()
k=dc.search_info('0972936543')
for p in k:
    print(p.hovaten)