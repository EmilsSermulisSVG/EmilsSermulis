import math
import random
radiuss = float(input("Ievadi riņķa līnijas rādiusu:"))        

print(radiuss)
rlgarums = radiuss * 2 * math.pi             #aprēķina riņķa līnijas garumu
print("riņķa līnijas garums:"'%.2f'%rlgarums)
rllaukums = math.pi * (math.pow(radiuss, 2))    #aprēķina riņķa līnijas laukumu
print("riņķa līnijas laukums:"'%.2f'%rllaukums)

katete1 = float(input("ievadi taisnleņķa trijstūra pirmā katetes garumu:"))
print(katete1)
katete2 = float(input("ievadi taisnleņķa trijstūra otrās katetes garumu:"))
print(katete2)


kapinata1 = math.pow(katete1,2)    #katešu kāpināšana
kapinata2 = math.pow(katete2,2)    #katešu kāpināšana


print("Taisnleņķa hipotenūzas garums ir: ", math.sqrt(kapinata1 + kapinata2))  # izvelk kvadrātsakni no katešu summas
gadijumsk ="Gadījuma skaitlis no 0 - 1: ", random.randint(0,1)
print(gadijumsk)
