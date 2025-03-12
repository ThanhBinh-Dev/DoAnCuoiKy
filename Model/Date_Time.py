class Date_Time:
    def __init__(self,ngaykham,giokham,slot_moi,slot_gioihan):
        self.ngaykham=ngaykham
        self.giokham=giokham
        self.slot_moi=slot_moi
        self.slot_gioihan=slot_gioihan
    def __str__(self):
        return f"{self.ngaykham}\t{self.giokham}"