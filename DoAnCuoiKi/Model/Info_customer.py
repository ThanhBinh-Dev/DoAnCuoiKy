import random

from DoAnCuoiKi.Model.Customer import Customer
from DoAnCuoiKi.Model.Date import Date
from DoAnCuoiKi.Model.DichVuKham import DichVuKham
from DoAnCuoiKi.Model.Doctor import Doctor
from DoAnCuoiKi.Model.Time import Time


class Info_customer(Customer, Date, Time, DichVuKham,Doctor):

    def __init__(self, hovaten, sdt, noikham, diachi, ngaykham, giokham, dichvu, thongtin,
                  madon=None, tinhtrang="Chưa Xác Nhận",bacsi=None, sdtbacsi=None,tendangnhap=None,matkhau=None):
        super().__init__(hovaten, sdt, noikham, diachi, thongtin)
        Date.__init__(self, ngaykham)
        Time.__init__(self, giokham)
        DichVuKham.__init__(self, dichvu)
        self.thongtin=thongtin
        madon_ngaunhien = (random.randint(1000, 10000))
        self.madon = madon if madon else f"#C{madon_ngaunhien}{sdt[-3:]}"
        self.tinhtrang=tinhtrang
        Doctor.__init__(self, bacsi, sdtbacsi)
        # Thêm thông tin đăng nhập
        self.tendangnhap = tendangnhap if tendangnhap else sdt
        self.matkhau = matkhau if matkhau else f"@{hovaten.split()[-1]}{sdt[-3:]}"


    def __str__(self):
        return (f"{self.hovaten}\t{self.sdt}\t{self.noikham}\t{self.diachi}\t{self.ngaykham}\t{self.giokham}"
                f"\t{self.dichvu}\t{self.thongtin}\t{self.madon}\t{self.tinhtrang}"
                f"\t{self.bacsi}\t{self.sdtbacsi}\t{self.tendangnhap}\t{self.matkhau}")

    def to_dict(self):
        return {
            "hovaten": self.hovaten,
            "sdt": self.sdt,
            "noikham": self.noikham,
            "diachi": self.diachi,
            "ngaykham": self.ngaykham,
            "giokham": self.giokham,
            "dichvu": self.dichvu,
            "thongtin": self.thongtin,
            "madon": self.madon,
            "tinhtrang": self.tinhtrang,
            "bacsi":self.bacsi,
            "sdtbacsi":self.sdtbacsi,
            "tendangnhap": self.tendangnhap,
            "matkhau": self.matkhau
        }