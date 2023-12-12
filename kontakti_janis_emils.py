kontakti = {"vards ": [], "nummurs":[]} #izveido vārdnīcu
kontakti["vards "] = ["Anna","Zane","Jānis","Gustavs"]
kontakti["nummurs"] = ["12835736","73423576","82345634","67374367"] #ievieto vārdnīcā vienības
cipars = input('ko vēlaties darīt?      1. drukāt     2. pievienot    3. izdzēst   4. iziet     5. parsteigums')
if cipars == '1':
    print('kontaktu saraksts: ')
    print('-------------------------------')
    for i in range(1):  
        print('Jūsu kontakti uz ekrāna: ')
        print(kontakti["vards "])
        print(kontakti["nummurs"])
elif cipars == '2':
    print('pievieno jaunu kontaktu: ')
    kontakts = input('ievadiet savu kontaktu: ') #iegūst jaunās vērtības priekš vārdnīcas.
    nummurs = input('ievadiet sava kontakta numuru: ')
    kontakti["vards "].append(kontakts)
    kontakti["nummurs"].append(nummurs) #ievieto jauno kontaktu vārdnīcā
elif cipars == '3':
    print('izdzēst kontaktu')
    dzest = input('ievadiet kontaktu, kuru vēlaties izdzēst: ')
    kontakti["vards "].remove(dzest) #izņem kontaktu no vārdnīcas.
elif cipars == '5':
    kaki = input('vai jūs esat kaķis? (j/n)')
    if kaki == 'j':
        print('tinies lapās!!!') #aizbiedē kaķus
    if kaki == 'n':
        print('tas ir labi!')
elif cipars == '4':
    exit() #beidz programmu.
