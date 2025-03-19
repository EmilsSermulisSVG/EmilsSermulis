# definē klasi dzīvnieks, kas ir saistīta ar kāju skaitu
class Dzivnieks:
    def __init__(self,kaju_skaits=0):
        self.kaju_skaits=kaju_skaits

    @classmethod # izmanto objektu izmantošanai ar noteiktu kāju skaitu
    def putns(kajas):
        return kajas(2)
        
    @classmethod 
    def majlops(kajas):
        return kajas(4)

    @classmethod 
    def simtkajis(kajas):
        return kajas(100)

    #metode, kas izdrukā kāju skaitu

    def izdrukat_kaju_sk(self):
        print(self.kaju_skaits)

# objekti(insatnce)

odze = Dzivnieks()
zoss = Dzivnieks.putns()
kaza = Dzivnieks.majlops()
simtkajis = Dzivnieks.simtkajis()
odze.izdrukat_kaju_sk()
zoss.izdrukat_kaju_sk()
kaza.izdrukat_kaju_sk()
simtkajis.izdrukat_kaju_sk()