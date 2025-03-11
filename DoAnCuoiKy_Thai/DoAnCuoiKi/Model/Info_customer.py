from DoAnCuoiKi.Model.Customer import Customer
from DoAnCuoiKi.Model.Date import Date
from DoAnCuoiKi.Model.DichVuKham import DichVuKham
from DoAnCuoiKi.Model.Time import Time


class Info_customer(Customer,Date,Time,DichVuKham):
    def __init__(self,hovaten,sdt,noikham,diachi,ngaykham,giokham,dichvu,thongtin):
        Customer.__init__(self, hovaten, sdt,diachi, noikham, thongtin)
        Date.__init__(self, ngaykham)
        Time.__init__(self, giokham)
        DichVuKham.__init__(self, dichvu)
    def __str__(self):
        return f"{self.hovaten}\t{self.sdt}\t{self.noikham}\t{self.diachi}\t{self.ngaykham}\t{self.giokham}\t{self.dichvu}\t{self.thongtin}"