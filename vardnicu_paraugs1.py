telefons = {
    "janis":213443,
    "Anna":123454,
    "Pēteris":652415
    }
#jānim ir 2 tel nr
#telefons.update(["janis",12341])
#print("Šis ir ")


#atslēgu virkni un fromkeys() metodi
#vārdnīca nenorādot vērtības

kk = {"viens", "divi", "trīs"}
dd = dict.fromkeys(kk)
print(kk)
val = 0    # vērtība būs visai vārdnīcai

dd = dict.fromkeys(kk,val)
print(dd)

#iveidot vārdnīcu kas satur sarakstu
valsts = {
    "Somija":["Helsinki","Tampere","Rovaniem"],
    "Latvija":["Sigulda", "Carnikava" ,"Cēsis"],
    "Dānijs":["Kopenhāgena","Ronna","Odense"]
          }
for atslega , vertiba in valsts.items():
    for i in vertiba:
        print("{}:{}".format(atslega,i))
