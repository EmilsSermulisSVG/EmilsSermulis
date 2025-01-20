#izveidot klasi bankaskonts
#ielikt 2 atribūtus- klienta vārds uhn atlikums
#klasē ir 2 metodes - iemaksāt(summa) - palielinās konta atlikumu par norādīto summu
#metode izņemt(summa)- samazina konta atlikumu par norādīto summu, ja pietiek līdzekļu
#objekti - klients Laura sākumā ir 100 eiro | iemaksā 50 pārbnauda atlikumu
#  izņem 30, pēc tam mēģina izņemt 200, lai notestētu gadījumu, kad nav līdzekļu

class Bankaskonts:
    def __init__(self,vards,atlikums):
        self.vards = vards # lauki
        self.atlikums = atlikums

    def iemaksat(self,summa):
        
        """"print(f"{self.vards} kontā ir {self.atlikums} eiro")
        iemaksas_summa = int(input("Cik eiro vēlaties iemaksāt"))
        print(f"Kontā tagad ir {self.atlikums+iemaksas_summa} eiro")"""

        self.atlikums+summa
        return f"Ielikti {summa} jaunais alikums {self.atlikums}"


    def izmaksas(self,summa):
        """"print(f"{self.vards} kontā ir {self.atlikums} eiro")
        izmaksas = int(input("Cik eiro vēlaties izņemt"))"""


        if summa > self.atlikums:
            return "Nepietiek līdzekļu"
        self.atlikums-=summa  #samazina konta tlikumu
        return f"Izņemti {summa} jaunais alikums {self.atlikums}"


konts = Bankaskonts("Laura",100)
print(konts.iemaksat(50))
print(konts.izmaksas(30))
print(konts.izmaksas(200))