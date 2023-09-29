import math

vardsuzvards = input("Programmu izstrādāja :")
print("Laukuma aprēķins ģeometriskām figūrām")

print("   ****")
amala = float(input("ievadiet malas a garmumu:"))
print(amala)

print("   ****")
bmala = float(input("ievadiet malas b garmumu:"))
print(bmala)

print("   ****")

augstums = float(input("ievadiet augstumu:"))
print(augstums)

reizinajums = amala * augstums     # aprēķina paralelograma laukumu un trijstūra malas un augstuma reizinājumu
trijsturaS = reizinajums / 2
print("Laukums trijstūrim :",trijsturaS)
absumma = (amala + bmala)            # saskaita trapeces malas
abmala = absumma / 2                 # malu summmu dala ar 2 ``
trapeceS = abmala * augstums         # malu dalijumu reizina ar augstumu un iegūs trapeces laukumu

print("Laukums trapecei :",trapeceS)
print("Laukums paralelogramam :",reizinajums)

print("Paldies!")