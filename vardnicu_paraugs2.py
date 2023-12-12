valsts = {
    "Somija":["Helsinki","Tampere","Rovaniem","Kemijarvi","jyvaskyle"],
    "Latvija":["Sigulda", "Carnikava" ,"Cēsis","Dobele","Ādaži"],
    "Dānija":["Kopenhāgena","Ronna","Odense","esbjerga","pilsēta5"]
          }

#izdrukāt vārdnīcas elementus piekļūstot vārdnīcia konkrētai atslēgai
for i in valsts["Somija"]:
    print(i)
for i in valsts["Latvija"]:
    print(i)
for i in valsts["Dānija"]:
    print(i)
    
    
#pirmās 3 pilsētas no Somijas

print(valsts["Somija"][:3])

#iegūt pēdēja 2 pilsētas no Latvijas

print(valsts["Latvija"][-2:])

#visas pilsētas no Somijas izņemot 3 pēdējās

print(valsts["Dānija"][:-3])

# no 2. līdz v5. pilsētai 

print(valsts["Dānija"][1:5])