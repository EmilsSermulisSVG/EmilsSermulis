class Dzivnieks:
    def __init__(self,vards,skana):
        self.vards = vards
        self.skana = skana

    def izdod_skanu(self):
        return f"{self.vards} saka {self.skana}!"
  
#objekti
kakis = Dzivnieks("Mince","Ņau")
gliemezis = Dzivnieks("Harijs","...")

print(kakis.izdod_skanu())
print(gliemezis.izdod_skanu())