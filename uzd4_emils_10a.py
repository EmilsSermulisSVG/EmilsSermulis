skaitli =[1,2,7,8,5,3,5,5,2,2,]
print(skaitli)
para_skaitli = 0
nepara_skaitli = 0  
garums = len(skaitli)


for i in range(0,garums):
    if skaitli[i]%2==0:
        para_skaitli +=1
        print("Pāra skaitļu skaits: ",para_skaitli)
    else:
        nepara_skaitli +=1
        print("Nepāra skaitļu skaits: ",nepara_skaitli)
