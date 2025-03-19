from abc import ABC,abstractmethod

# vispārīga datu struktūra, kas nepieciešama visām grāmatām

class Gramata(ABC):   # abstrakta klase ar metodi gramatas_dati
    @abstractmethod
    def gramatas_dati(self):
        pass

# izveidot 2 apakšklases kur katra metodi(gramatas_dati) realizē citādāk

class Hobbits(Gramata):
    def gramatas_dati(self):
        print("Hobbits,666lpp")
    
class GredzenPavelnieks(Gramata):
    def gramatas_dati(self):
        print("Gredzena Pavelnieks,999lpp")
    

gramata1=Hobbits()
gramata1.gramatas_dati()
gramata2=GredzenPavelnieks()
gramata2.gramatas_dati()