#izveidot tukšu vārdnīcu
vardnica = {
    "a":4,
    "b":6
}

ievade_atsl = input("ievadiet atslēgu: ")
ievade_vert = input("ievadiet vērtību: ")

#pārbauda lietotāja ievadi un rediģē vārdnīcu
if ievade_atsl in vardnica:
    vardnica[ievade_atsl] = ievade_vert
    print("Vārdnīca tika atjaunināta!")
    
else:
    vardnica[ievade_atsl] = ievade_vert
    print("Jauns pāris tika pievienots vārdnīcai!")
    
print("Atjauninātā vārdnīca: ",vardnica)