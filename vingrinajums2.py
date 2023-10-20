atbilde = "j"
while atbilde =="j":
    print("nekusties")
    atbilde = input("vai brismoniws ir draudzīgs?(j/n)")
print("bēdz prom!")



""""
#pārbaudīt vai lietotājs prot reizināt ar 7
#programma atkŗto darbību līdz brīdim kad uzadoti 12 jautājumi
reiz = int(input("reizinātājs"))
for i in range(1,13): #ciklā mainīgais no viens līdz 12
    print("Cik ir",i,"x",reiz,"?")
    minejums = input()
    if minejums == "stop":
        break #pārtrauc programmu
    if minejums =="izlaist":
        print("tiek izlaists")
        continue #izlaiž jautājumu un turpina ciklu tālāk
    atb = i * reiz
    if int(minejums) == atb:
        print("pareizi")
    else:
        print("Nē tas ir",atb)
        # ja ir nepareizi tad atgriežas pie jautājuma
        #reizinājumu uevada lietotājs
    """