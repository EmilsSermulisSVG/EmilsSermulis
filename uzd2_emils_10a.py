""""dienas={
    "1dec":4,
    "2dec":2,
    "3dec":3,
    "4dec":5,
    "5dec":4,
    "6dec":1,
    "7dec":0, 
}"""
nedelas_diena = input("ievadiet datumu no 1. līdz 7. decembrim (piemēram: 1.decembris), atlikušais mēģinājumu skaits: ")

dienas = {"datums":[],"temperatura":[]} 
dienas["datums"] = ["1.decembris","2.decembris","3.decembris","4.decembris","5.decembris","6.decembris","7.decembris",]             
dienas["temperatura"] = [4,1,5,3,2,6,0]
len(dienas["datums"])
len(dienas["temperatura"])

""""nedelas_diena = input("ievadiet datumu no 1. līdz 7. decembrim (piemēram: 1.decembris)")
while nedelas_diena != dienas["datums"]:
    i = 1
    for i in range (4):
        print("atlikušais mēģinājumu skaits: ",4-i)
        nedelas_diena = input("ievadiet datumu no 1. līdz 7. decembrim (piemēram: 1.decembris), atlikušais mēģinājumu skaits: ")
"""
        
        
        
if dienas["datums"][0]== "1.decembris":
    print(dienas["datums"][0],"Celsija skalā ir ",dienas["temperatura"][0])
    farenheita = dienas["temperatura"][0] * (9/5) +32
    print(["datums"][0],"temperatūra Fāreinheita sklā ir: ",farenheita)
    
elif dienas["datums"][1]== "2.decembris":
    print(dienas["datums"][1],"Celsija skalā ir ",dienas["temperatura"][1])
    farenheita = dienas["temperatura"][1] * (9/5) +32
    print(["datums"][1],"temperatūra Fāreinheita sklā ir: ",farenheita)
    
elif dienas["datums"][2]== "3.decembris":
    print(dienas["datums"][2],"Celsija skalā ir ",dienas["temperatura"][2])
    farenheita = dienas["temperatura"][2] * (9/5) +32
    print(["datums"][2],"temperatūra Fāreinheita sklā ir: ",farenheita)
    
    
    
