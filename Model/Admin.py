class Admin:
    def __init__(self, tendangnhap, matkhau, sodienthoai):
        self.tendangnhap = tendangnhap
        self.matkhau = matkhau
        self.sodienthoai = sodienthoai
    def __str__(self):
        return f"{self.tendangnhap}\t{self.matkhau}\t{self.sodienthoai}"