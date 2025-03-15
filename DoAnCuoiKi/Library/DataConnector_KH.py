from DoAnCuoiKi.Library.JsonFileFactory import JsonFileFactory
from DoAnCuoiKi.Model.Info_customer import Info_customer


class DataConnector_QLKH:
    def get_info_customer(self):
        jff=JsonFileFactory()
        filename='../Dataset/Info_Customer.json'
        list_info=jff.read_data(filename,Info_customer)
        return list_info
    def search_info(self,sdt):
        list_info=self.get_info_customer()
        info_cus=[]
        for info in list_info:
            if str(sdt)==str(info.sdt):
                info_cus.append(info)
        return info_cus

