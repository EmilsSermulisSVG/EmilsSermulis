from abc import ABC,abstractmethod
class SkolasDarbinieki(ABC): #Abstraktā klase
    def __init__(self,vards,uzvards): #Bāzes klase ar laukiem
        self.vards= vards
        self.uzvards=uzvards
    @abstractmethod
    def apraksts(): #metode, kas būs visās apakš klasēs
        pass
class Skolotajs(SkolasDarbinieki):
    def __init__(self,vards,uzvards,prieksmets):
        super().__init__(vards,uzvards)
        self.prieksmets=prieksmets #papildus lauks
    def apraksts(self): #mantotā metode
        return f"{self.vards} {self.uzvards} ir Skolotājs kura māca {self.prieksmets}"
class Apkopeja(SkolasDarbinieki):
    def apraksts(self):
        return f"{self.vards} {self.uzvards} ir Apkopēja kura tīra skolu."
class IT_cilveks(SkolasDarbinieki):
    def apraksts(self):
        return f"{self.vards} {self.uzvards} ir ITišņiks kurš dara IT lietas."
class Lietvedis(SkolasDarbinieki):
    def apraksts(self):
        return f"{self.vards} {self.uzvards} ir Lietvede kura audzina 11.a klasi."

darbinieki = [Skolotajs("Inta","Janule","Matemātika"),Apkopeja("Ilze","Krūmiņa"),IT_cilveks("Roberts","Ozols"),Lietvedis("Anda","Lāce")] #saraksts ar visiem objektiem
for darbinieks in darbinieki: #for ciklu izraksta visus objektus sarakstā
    print(darbinieks.apraksts())

with open("darbinieki.txt","w",encoding="utf8") as file: #saglabā failā darbinieks.txt
    for darbinieks in darbinieki: #for ciklu izraksta visus objektus sarakstā
        file.write(darbinieks.apraksts())
        file.write("\n")
        