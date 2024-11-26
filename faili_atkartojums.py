#1.uzd
#saglabāt datus sarakstā

""""names = []
for i in range(3):
    names.append(input("whats your name?: "))

#atgriež sakārtotus
for name in sorted(names):
    print(f"Hello {name} ")"""

#2.uzd
# informāciju no konsoles ieraksta failā

""""
name = input("whats your name?: ")
file = open("names.txt","w", encoding="utf8") #w(write) izveido failu un ieraksta datus 
file.write(name)
file.close() # ja izmanto file=open tad aizver failu ciet file.close()

#a režīmā izveido failu, bet info pievieno klāt
file.write(f"{name2}\n")
file.close()# ja izmanto file=open tad aizver failu ciet file.close()"""

#3.uzd
#lieto context manager-fails nav jāaizver
""""name = input("whats your name?: ")
with open("names.txt","a",encoding="utf8") as file: # a (append)
    file.write(f"{name}\n")"""

#4.uzd
# nolassa info no faila
""""with open("names.txt","r",encoding="utf8")as file: # r var nelikt, noklusējuma režīms
    for line in file: # line vietā raksta jebko
        print("hello,",line.rstrip())
"""

#5.uzd
#atgriezt sakārtotus datus no faila

names = []
with open("names.txt",encoding="utf8")as file:
    for line in file:
        names.append(line.rstrip())

#atgriež sakārtotus
for name in sorted(names):
    print(f"Hello {name} ")