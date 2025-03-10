class Customer:
    def __init__(self,hovaten,sdt,noikham,diachi="None",thongtin="None"):
        self.hovaten = hovaten
        self.sdt = sdt
        self.noikham = noikham
        self.diachi = diachi
        self.thongtin = thongtin
    def __str__(self):
        return f"{self.hovaten}\t{self.sdt}\t{self.noikham}\t{self.diachi}\t{self.thongtin}"
