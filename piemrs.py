import math
import random
skaitlis = 43.7
print("Noapaļots uz leju:",math.floor(skaitlis))
print("Noapaļots uz augšu:",math.ceil(skaitlis))

print("Mainīgā pakāpe:",math.pow(skaitlis,2)) #kāpināšana
print(math.pow(4,6)) #pirmais sk ir tas ko kāpina otrais ir...
pakape = 3
print(math.pow(skaitlis, pakape))

print("Kvadrātsakne: ",math.sqrt(skaitlis))
#skaitļu formatēšana
x = 23434/123
print("x:",x)
print("formatēts x:"  "%.3f"%x) # 1. variants
print("formatēts x:"  "{:3f}".format(x)) #2. varinats

cipars = random.random() # 0.1 - 10
print(cipars)

cipars2 = random.randint(1,50)
print(cipars2)
