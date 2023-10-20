
print(" Veikala preces:"'\n',"piens" '\n',"cukurs" '\n',"milti" '\n',"maize" '\n',"makaroni" '\n',"paprika")



preces_daudzums = int(input("Ievadi cik preces tu pirksi: "))
if preces_daudzums > 0:
   
    while preces_daudzums > 0:
        preces_daudzums = preces_daudzums - 1
        input("Ievadi preces nosuakumu: ")
        cena = float(input("ievadi preces cenu: "))
        
        if preces_daudzums == 0:
            saraksts = input("Vai viss ir nopirkts sarakstā?(j/n)")
            
            while saraksts =="n":
                (input("ievadi preces nosuakumu"))
                cena2 = float(input("ievadi preces cenu: "))
                saraksts = input("Vai viss ir nopirkts sarakstā?(j/n)")
            if saraksts =="j":
                atlaides = input("gribi zināt atlaižu variantus?(j/n)")
                if atlaides =="j":

                    print("atlaižu varianti:"'\n',"1. 30%" '\n',"2. 40% ar karti" '\n',"3. 20%, bet ar karti 50%" '\n',"4. 30% ja pērk 3 preces vai vairāk" '\n',"5. katra 2. prece par brīvu")
                    karte = input("vai jums ir karte? (j/n)")
                    if karte =="j":
                        print("atlaižu varianti:"'\n',"1. 40% ar karti" '\n',"2. 20%, bet ar karti 50%")
                    elif karte =="n":
                        print("atlaižu varianti:"'\n',"1. 30%" '\n',"2. 30% ja pērk 3 preces vai vairāk" '\n',"3. katra 2. prece par brīvu")
                        #for i in range(preces_daudzums):
                        