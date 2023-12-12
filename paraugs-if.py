# izveidot vārnīcu ar datiem par automašīnu (4)

auto = {
    "zīmols":"Volvo",
    "krāsa":"Pelēks",
    "gads":2000,
    "modelis":"xc90"
}
dati = input("Ievadiet zīmolu, lai pārbaudītu: ")
if dati == auto["zīmols"]:
    print("🚗 Ir vārdnīcā!")
elif dati == auto.values():
    print("🚗 ir kā vērtībā")
else:
    print("Šāda 🚗 nav")