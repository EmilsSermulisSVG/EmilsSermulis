import math
print("Ābolu ievārijuma recepte vienai burkai :"'\n',"3kg ābolu" '\n',"1kg cukurs" '\n',"500ml ūdens" '\n',"1 citrons" '\n',"5 ml mandeļu ekstrakts" '\n',"10g kanēlis")
produkti = str(input("vai tev ir viss nepieciešamais? (j/n)"))

cukura_cena = 1.29
citrona_cena = 2.39
ekstrakta_cena = 6.49
kanela_cena = 1.89

if produkti =="j":
    aboli = int(input("Ievadi cik kg ābolu tev ir"))
    cukurs = int(input("Ievadi cik cukurs tev ir"))
    udens = int(input("Ievadi cik ml udehns tev ir"))
    citrons = int(input("Ievadi cik citronu tev ir"))
    ekstrakts = int(input("Ievadi cik ml madeļu ekstrakts tev ir"))
    kanelis = int(input("Ievadi cik g kanēļa tev ir"))
    if aboli >=3 and cukurs >= 1 and udens >= 500 and citrons >= 1 and ekstrakts >= 5 and kanelis >= 10:          #pārbauda vai visi produkti ir nepieciešamā daudzumā
        
        
        print("tu vari taisīt ievārijumu")         # aprēķina
        aboli_burkai = aboli//3
        cukurs_burkai = cukurs//1
        udens_burkai = udens//500
        citrons_burkai =  citrons//1
        ekstrakts_burkai = ekstrakts//5
        kanelis_burkai = kanelis//10
        
        

    else:
        print("tev jāiet uz tirgu pakaļ vajadzīgajiem produktiem")
            
            
                
elif produkti == "n":
    trukst_cukurs = str(input("vai tev ir pietiekami daudz cukurs?(j/n)"))
    trukst_citroni = str(input("vai tev ir pietiekami daudz citronu?(j/n)"))
    trukst_ekstarkts = str(input("vai tev ir pietiekami daudz ekstarkts?(j/n)"))
    trukst_kanelis = str(input("vai tev ir pietiekami daudz kanēļa(j/n)"))
    if trukst_cukurs =="n":
        print("tev jāiet uz tirgu pakaļ cukuram un tas tev izmaksās:", cukura_cena)
    elif trukst_citroni =="n":
        print("tev jāiet uz tirgu pakaļ cukuram un tas tev izmaksās:", citrona_cena)
    elif trukst_ekstarkts == "n":
        print("tev jāiet uz tirgu pakaļ cukuram un tas tev izmaksās:", ekstrakta_cena)
    elif trukst_kanelis == "n":
        print("tev jāiet uz tirgu pakaļ cukuram un tas tev izmaksās:", kanela_cena)
    else:
        print("tev ir viss nepieciešamais")



    
    

