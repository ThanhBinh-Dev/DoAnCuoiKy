class Doctor:
    def __init__(self, hovaten, sodienthoai):
        self.hovaten = hovaten
        self.sodienthoai = sodienthoai
    def __str__(self):
        return f"{self.hovaten}\t{self.sodienthoai}"