from DoAnCuoiKi.Library.JsonFileFactory import JsonFileFactory
from DoAnCuoiKi.Model.Info_customer import Info_customer


class DataConnector_QLKH:
    def get_info_customer(self):
        info_customer = []
        jff=JsonFileFactory()
        filename = "../Dataset/Info_Customer.json"
        info_customer=jff.read_data(filename,Info_customer)
        return info_customer
    def search_info(self,sdt):
        list_info=[]
        self.info_customer = self.get_info_customer()
        for info in self.info_customer:
            if str(info.sdt)==str(sdt):
                list_info.append(info)
        return list_info

