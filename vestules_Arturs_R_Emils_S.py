from abc import ABC, abstractmethod
class Persona(ABC):
    def __init__(self,name,e_pasts):
        self.name=name
        self.e_pasts=e_pasts
class Vestule:
    def __init__(self,nosutitajs,sanemejs,vestule_saturs):
        self.nosutitajs=nosutitajs
        self.sanemejs=sanemejs
        self.vestule_saturs=vestule_saturs
class VestulesSuta(ABC):
    def sutit_vestuli():
        pass
    def sanemt_vestuli():
        pass
class Pastnieks(VestulesSuta):
    def __init__(self,nosutitajs,sanemejs,vestule_saturs):
        self.nosutitajs=nosutitajs
        self.sanemejs=sanemejs
        self.vestule_saturs=vestule_saturs
    def sutit_vestuli(self):
        print(f"Vēstule no: {self.nosutitajs}")
        print(f"Vēstule uz: {self.sanemejs}")
        print(f"Saturs: {self.vestule_saturs}")
        print(f"Vēstule nosūtīta ar pastnieka palīdzību.")
    def sanemt_vestuli(self):
        print(f"Vēstule saņemta no: {self.nosutitajs}")
        print(f"Vēstule uz: {self.sanemejs}")
        print(f"Saturs: {self.vestule_saturs}")

persona1 = Persona("Jānis Zibens","zibens.sper@svg.lv")
persona2 = Persona("Zana Puķe","pukes.zied@svg.lv")
pastnieks = Pastnieks(persona1[0],persona2[1],"Lūdzu rrrr")
pastnieks.sutit_vestuli()
pastnieks.sanemt_vestuli()
