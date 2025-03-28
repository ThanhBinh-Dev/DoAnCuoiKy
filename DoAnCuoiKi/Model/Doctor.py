class Doctor:
    def __init__(self, bacsi, sdtbacsi):
        self.bacsi = bacsi
        self.sdtbacsi = sdtbacsi
    def __str__(self):
        return f"{self.bacsi}\t{self.sdtbacsi}"