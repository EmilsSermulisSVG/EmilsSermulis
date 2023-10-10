print("Ābolu ievārijuma recepte:"'\n',"3kg ābolu" '\n',"1kg cukurs" '\n',"500ml ūdens" '\n',"1 citrons" '\n',"5 ml mandeļu ekstrakts" '\n',"10g kanēlis")
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
    if aboli >=3 and cukurs >= 1 and udens >= 500 and citrons >= 1 and ekstrakts >= 5 and kanelis >= 10:
        print("tu vari taisīt ievārijumu")
        
        
    else:
        print("tev jāiet uz tirgu pakaļ vajadzīgajiem produktiem")
            
            
            
            

elif produkti == "n":
    trukst_cukurs = str(input("vai tev ir pietiekami daudz cukurs?(j/n)"))
    trukst_citroni = str(input("vai tev ir pietiekami daudz citronu?(j/n)"))
    trukst_ekstarkts = str(input("vai tev ir pietiekami daudz ekstarkts?(j/n)"))
    trukst_kanelis = str(input("vai tev ir pietiekami daudz kanēļa(j/n)"))
    if trukst_cukurs =="j":
        print("tev jāiet uz tirgu pakaļ cukuram un tas tev izmaksās:", cukura_cena)
    elif trukst_citroni =="j":
        print("tev jāiet uz tirgu pakaļ cukuram un tas tev izmaksās:", citrona_cena)
    elif trukst_ekstarkts == "j":
        print("tev jāiet uz tirgu pakaļ cukuram un tas tev izmaksās:", ekstrakta_cena)
    elif trukst_kanelis == "j":
        print("tev jāiet uz tirgu pakaļ cukuram un tas tev izmaksās:", kanela_cena)
        



    
    

