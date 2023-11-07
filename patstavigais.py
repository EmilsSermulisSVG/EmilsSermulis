""""izveido 3 sarakstus : lietotājs pats norādīs cik lementus likt sarakstā,
pirmā un otrā saraksta vērtības ievada lietotājs
trešā sarakstavērtības iegūst apviwenojot pirmos 2 sarakstus
katra saraksta saturu glīti parādīt uz ekrāna"""

saraksts1 = []
saraksts2 = []
saraksts3 = []





saraksta_elementi = int(input("ievadi cik elemneti būs tavos sarakstos : "))

for i in range (saraksta_elementi):
    lieta1 = input("ievadi saraksta elemtus")
    saraksts1.append(lieta1)
print("pirmāsaraksta elementi: ",saraksts1)
    
    
    
    
saraksta_elementi2 = int(input("ievadi cik elemneti būs tavos sarakstos : "))
   
for j in range (saraksta_elementi2):
    lieta2 = input("ievadi saraksta elemtus")
    saraksts2.append(lieta2)
print("pirmāsaraksta elementi: ",saraksts2)

saraksts3 = saraksts1 + saraksts2
print(saraksts3)
