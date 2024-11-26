#ierakstīt teksta failā(no programmas) vārdu uzvārdu un vecumu, dot iespēju izvēlēties 
#1 - pievienot datus
#2 - izvada datus
#3 - izvadīt konsolē sakārtot, parādīt datus pēc vecuma
#4 - iziet
# apstrādāt kļūdas
# pietiek ar 3 funkcijām, def sakārtot pēc vecuma, def parādīt sakārtotus datus
while True:
    print("\n Izvēlēties opciju: ")
    print("1 - Pievienot datus")
    print("2 - Parādīt datus")
    print("3 - Iziet")

    izvele = input("Izvēle: ")

    if izvele =="1": # pievieno datus failam
        vards =input("Ievadiet vārdu: ")
        uzvards =input("Ievadiet uzvārdu: ")
        vecums = int(input("Ievadiet vecumu: "))\
        #datus saglabā teksta failā

        with open("praktiskais_atbildes.txt","a",encoding="utf8") as file:
            file.write(f"{vards} {uzvards} {vecums}\n")
        print("Dati ir pievienoti")

    elif izvele=="2": # nolasa datus no faila
        try:
            with open("praktiskais_atbildes.txt","r",encoding="utf8") as file:
                dati = file.readlines()

            if not dati: #pārbauda vai failā ir dati
                print("Fails ir tukšs, pievienojiet datus")
            else:
                print("\nDati no faila")
                for ieraksts in dati:
                    print(ieraksts.strip())

        except FileNotFoundError: # Ja fails nepastāv
            print("Fails nepastāv")

    elif izvele =="3":
        print("Izvēle tiek pārtraukta")
        break
    else:
        print("Nepareiza izvēle")