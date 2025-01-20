import csv
from datetime import datetime

class Rekins:
    def __init__(self,klients,veltijums,izmers,materials):
        self.klients = klients
        self.veltijums = veltijums
        self.izmers = izmers        # platums garums augstums
        self.materials = materials
        self.laiks=datetime.now().strftime("%Y-%m-%d %H:%M%S")
        self.darba_samaksa = 15
        self.PVN = 21
        #self.summa = 0   # aprēķinās vēlāk, izsaucot aprekins()
        self.summa=self.aprekins() # aprēķinās pēc objekta izveidošanas, pamatojoties uz citiem parametriem


    def aprekins(self): #self atsaucas uz pašreizējo objektu, tātad uz visiem atribūtiem, kas objektam pieejami
        # "izpakot" izmērus
        platums, garums, augstums = self.izmers
        veltijuma_garums = len(self.veltijums)
        produkta_cena = (veltijuma_garums*1.20)+(platums/100 * garums/100 * augstums/100)/3*self.materials
        PVN_summa = (produkta_cena + self.darba_samaksa)*self.PVN
        rekina_summa = (produkta_cena + self.darba_samaksa) + PVN_summa
        return round(rekina_summa,2)


    def izdruka(self):
        print(f"Klients: {self.klients}\nVeltījums: {self.veltijums}\nIzmers: platums ={self.izmers[0]} garums ={self.izmers[1]} augstums ={self.izmers[2]}\nMaterials: {self.materials}\nLaiks: {self.laiks}\nPVN: {self.PVN}\nDarba samaksa {self.darba_samaksa}\nRēķins: {self.summa}\n")

    
    def saglabat(self):
        datnes_nosaukums=f"rekins_{self.klients}_{datetime.now().strftime('%Y-%m-%d')}.csv"
        with open(datnes_nosaukums,"w",encoding="utf8",newline=" ")as fails:
            rakstitajs = csv.writer(fails)
            rakstitajs.writerow(["Klients ","Veltījums ","izmers ","Izveidošnas laiks ","Cena ","Darba samaksa ","PVN ","Summa "]) 
            rakstitajs.writerow([self.klients, self.veltijums, f"{self.izmers[0]}x{self.izmers[1]}x{self.izmers[2]}", self.laiks, self.materials, self.darba_samaksa, self.PVN, self.summa])

            print(f"Rēķins saglabāts failā: {datnes_nosaukums}")

    
klients = input("Klients: ")
veltijums = input("Veltijums: ")
platums = int(input("Platums: "))
garums = int(input("Garums: "))
augstums = int(input("Augstums: "))
materials = float(input("Matriala cena: "))

# jauna rēķina objekta izveidošana

rekins=Rekins(klients,veltijums,[platums,garums,augstums],materials)
#saglabat un izdrukat rēķinu
rekins.saglabat()
rekins.izdruka()
#rekins.aprekins()  ja pie laukiem liek, ka summa=0
