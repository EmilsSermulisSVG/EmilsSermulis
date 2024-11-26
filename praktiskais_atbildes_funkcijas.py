#ierakstīt teksta failā(no programmas) vārdu uzvārdu un vecumu, dot iespēju izvēlēties 
#1 - pievienot datus
#2 - izvada datus
#3 - izvadīt konsolē sakārtot, parādīt datus pēc vecuma
#4 - iziet
# apstrādāt kļūdas

def parbauit_vardu(vards): #pārbauda vai dati sastāv tikai no burtiem
    if not vards.isalpha():
        print("Nepareizi dati: vārdā drīkst būt tikai burti")
        return False
    return True

def parbaudit_vecumu(vecums): # pārbauda vai deīgi dati
    if not vecums.isdigit():
        print("vecums var būt tikai skaitlis")
        return False
    if int(vecums)<=0:
        print("vecumam jābūt lielākam par 0")
        return False
    return True


def normalizet_vardu(vards):
    return vards.strip().capitalize() # noņem liekās atstarpes un lielo uzliewk lielo sākuma burtu


def dublikats(vards,uzvards,vecums,faila_nosaukums):
    try:
        with open(faila_nosaukums,"r",encoding="utf8") as file:
            dati = file.readlines()
        ieraksts = f"{vards},{uzvards},{vecums}\n"
        return ieraksts in dati
    except FileNotFoundError:
        return False # fails nav izveidots, tātad dublikātu nav



def pievienot_datus_failam(faila_nosaukums):
    try:

        with open(faila_nosaukums,"a",encoding="utf8") as file:
            while True:
                vards =input("Ievadiet vārdu: ")
                if parbauit_vardu(vards):
                    vards = normalizet_vardu(vards)
                    break

            while True:
                uzvards =input("Ievadiet uzvārdu: ")
                if parbauit_vardu(uzvards): 
                    uzvards = normalizet_vardu(uzvards)
                    break

            while True:
                vecums = input("Ievadiet vecumu: ")
                if parbaudit_vecumu(vecums):
                    break
            if dublikats(vards,uzvards,vecums,faila_nosaukums):
                print("Šis ieraksts jau pastāv")
                return

            file.write(f"{vards}, {uzvards}, {vecums}\n")#datus saglabā teksta failā
            print("Dati ir pievienoti")

    except Exception as kluda:
        print(f"Kļūda, saglabājot datus failā {kluda}")



def paradit_datus(faila_nosaukums):
    try:
        with open(faila_nosaukums,"r",encoding="utf8") as file:
            dati = file.readlines()

        if not dati: #pārbauda vai failā ir dati
            print("Fails ir tukšs, pievienojiet datus")
        else:
            print("\nDati no faila")
            for ieraksts in dati:
                print(ieraksts.strip())

    except FileNotFoundError: # Ja fails nepastāv
        print(f"Fails {faila_nosaukums} nepastāv")



def iegut_vecumu_no_datiem(ieraksts):
    try:
        vecums = int(ieraksts.strip().split(",")[-1])
        return vecums
        # ja formāts nav pareizs, atgriež 0
    except(IndexError,ValueError):
        return 0



def sakartot_izvadit(faila_nosaukums):
    try:
        with open(faila_nosaukums,"r",encoding="utf8") as file:
            dati = file.readlines()
        if not dati: #pārbauda vai failā ir dati
            print("Fails ir tukšs, pievienojiet datus")
        else: # kārtošana
            sakartoti_dati = sorted(dati,key= iegut_vecumu_no_datiem) # kārto pēc funkcijas
            print("\nPēc vecums sakārtoti dati")
            for ieraksts in sakartoti_dati:
                print(ieraksts.strip())
    except FileNotFoundError: # Ja fails nepastāv
        print(f"Fails {faila_nosaukums} nepastāv")



def izvele():
    faila_nosaukums = "praktiskais_atbildes_funkcijas.txt"
    while True:
        print("\n Izvēlēties opciju: ")
        print("1 - Pievienot datus")
        print("2 - Parādīt datus")
        print("3 - parādīt sakārtotus datus pēc vecums")
        print("4 - Iziet")

        izvele = input("Izvēle: ")

        if izvele =="1": # pievieno datus failam
            pievienot_datus_failam(faila_nosaukums)
        elif izvele =="2": # nolasa datus no faila
            paradit_datus(faila_nosaukums)
        elif izvele =="3":
            sakartot_izvadit(faila_nosaukums)
        elif izvele =="4":
            print("Izvade tiek pārtraukta")
            break
        else:
            print("Nepareiza izvēle")

izvele()

