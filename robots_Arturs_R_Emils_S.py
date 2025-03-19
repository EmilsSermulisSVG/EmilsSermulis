from abc import ABC, abstractmethod
import random
class Robot(ABC): #izveido abstrakt bāzes klasi
    @abstractmethod
    def baterijas_status(self):
        pass
    def uzdevums(self):
        pass
class CleaningRobot(Robot): #apakšklase kas manto abstrakto klasi
    def __init__(self,name): 
        self.name=name 
        self.baterijas_limenis=random.randint(0,100)#Izmantojot random.randint iegūst skaitli starp 0 un 100
    def baterijas_status(self):
        print(f"{self.name} baterijas līmenis: {self.baterijas_limenis}%") #izraksta nosaukumu un baterijas līmeni
    def uzdevums(self):
        print(f"{self.name} tīra telpu ar putekļsūcēju!")

class SecurityRobot(Robot): #apakšklase kas manto abstrakto klasi
    def __init__(self,name):
        self.name=name
        self.baterijas_limenis=random.randint(0,100)
    def baterijas_status(self):
        print(f"{self.name} baterijas līmenis: {self.baterijas_limenis}%") #izraksta nosaukumu un baterijas līmeni
    def uzdevums(self):
        print(f"{self.name} patrulē teritorijā un seknē apkārtni!")

class CookingRobot(Robot): #apakšklase kas manto abstrakto klasi
    def __init__(self,name):
        self.name=name
        self.baterijas_limenis=random.randint(0,100)
    def baterijas_status(self):
        print(f"{self.name} baterijas līmenis: {self.baterijas_limenis}%") #izraksta nosaukumu un baterijas līmeni
    def uzdevums(self):
        print(f"{self.name} hatavo gardu ēdienu!")

roboti = [CleaningRobot("CleanerRobot"),SecurityRobot("RoboGuard"),CookingRobot("ChefBot")] #ievada visu objektus sarakstā
for robot in roboti: #ad for ciklu izraksta visus objektus sarakstā
    robot.baterijas_status()
    robot.uzdevums()
    print("------------------------------------------------")