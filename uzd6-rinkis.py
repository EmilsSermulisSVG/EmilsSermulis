class Rinkis:
    def __init__(self,radiuss):
        self.radiuss = radiuss

    
    def iestatit_radiusu(self,radiuss):
        if radiuss <= 0:
            self.radiuss = 1
        else:
            self.radiuss = radiuss
    
    def izvadit_radiusu(self):
        return self.radiuss

    def diametrs(self):
        return self.radiuss*2

radiuss = float(input("Ievadiet radiusu: "))

rinkis = Rinkis(radiuss)    #objekts
print("Riņķa rādiuss ",rinkis.izvadit_radiusu())
print("Riņķa diametrs ",rinkis.diametrs())
