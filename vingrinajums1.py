#izdrukāt skaitļus 0,1,2,3,4,5,

"""for i in range(6):    #defaultā sākasies ar 0
    print(i)
print("------------------")
#izdrukāt  3,5.7
for i in range(3,8,2):
    print(i)
    
n = int(input("ievadi skaitli:"))
for i in range(1,11):
    print(n,"+",i,"=",n+i)
print("------------------")
#strast skaitļu 2 un 4 dalītājus
#uz ekrāna parādīt tos kas dalās ar 2 un tos kas dalas gan 4 gan 2
#range 50"""

for i in range(51):
    if i%2==0 and i%4==0:
        print(i,":dalos ar 2 un 4")
    elif i%2==0:
        print(i,":dalos ar 2")
    else:
        print(i)
    