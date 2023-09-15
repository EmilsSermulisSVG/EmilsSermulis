skaitlis=(int(input("Ievadi divciparu skaitli:")))       #ļauj lietotājam ievadīt ciparus
pirmais_cipars=skaitlis//10                    #apreiķina skaitļa pirmo ciparu izmantojot dalīšanu
print("pirmais cipars ir:", pirmais_cipars)    #izvada pirmo ciparu
otrais_cipars=skaitlis%10                      #aprēķina skaitļa otro ciparu izmantojot atlikuma aprēķināšanu
print("otrais cipars ir:", otrais_cipars)      #izvada otro ciparu
summa = pirmais_cipars + otrais_cipars
print("Ciparu summa ir:",summa)