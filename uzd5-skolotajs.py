class Skolotajs:
    def __init__(self,vards,prieksmets): #konstruktors
        self.vards = vards          #lauks, atribūta
        self.prieksmets = prieksmets

    def iepazistinatArSevi(self):
        print(f"Sveiki, mani sauc {self.vards}")
        
    def izliktVertejumu(self,punkti):
        if punkti >5:
            return f"Priekšmets {self.prieksmets} ir nokartots"
        else:
            return f"Priekšmets {self.prieksmets} nav nokartots"


#objektu izveidošana
rinalds = Skolotajs("Rinalds","Matemātika")
sandra = Skolotajs("Sandra","Literatūra")

rinalds.iepazistinatArSevi()
print(rinalds.izliktVertejumu(10))

sandra.iepazistinatArSevi()
print(sandra.izliktVertejumu(3))