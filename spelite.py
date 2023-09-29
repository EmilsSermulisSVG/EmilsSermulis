import random
# akmens šķēres papīrīts
gajieni = ["akmens", "šķēres", "papīrs"] #saraksts
while True:
    cilveka_gajiens = input("ievadi savu gājienu") 
    datora_gajiens = random.choice(gajieni)
    print("Cilvēks:",cilveka_gajiens, "vs dators", datora_gajiens)
    if cilveka_gajiens == datora_gajiens:
        print("Neizšķirts")
    elif cilveka_gajiens == "akmens" and datora_gajiens == "šķēres":
        print("Cilvēks uzvar")
    elif cilveka_gajiens == "šķēres" and datora_gajiens == "papīrs":
        print("Cilvēks uzvar")
    elif cilveka_gajiens == "papīrs" and datora_gajiens == "akmens":
        print("Cilvēks uzvar")
    else :
        print("Dators uzvar")
  