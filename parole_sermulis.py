
parole = "12345"
lietotajs = "skolens"

lietotajs = input("lūdzu ievadiet lietotājvārdu: ")   # lietotājs ir "skolens"!!!!!!!!!
parole = input("lūdzu Ievadiet paroli")

if lietotajs == "skolens" and parole == "12345":      # ja lietotājvārds un parole ir pareiz 
   print("pielsēgšanās veiksmīga")


while lietotajs != "skolens" and parole != "12345":       #ja lietotajvārds un parole nav pareiza tad ir vēl 5 mēģinājumi 
    i = 1
    for i in range(5):
        print("Atlikušais mēģinājumu skaits: ",5-i)         
        lietotajs2 = input("lūdzu ievadiet lietotājvārdu: ") 
        parole2 = input("lūdzu Ievadiet paroli: ")
        if lietotajs2 == "skolens" and parole2 =="12345":           #ja lietotajvārds un parole ir pareiza tad programma turpinās un pārtrauc ciklu
            print("pielsēgšanās veiksmīga")
            skaitlis1 = input("Ievadi 1. skaitli")
            skaitlis2 = input("Ievadi 2. skaitli")
            break

          
    if i == 0:                                        
            print("Programmas beigas")
            break
    elif lietotajs2 or parole2== "stop" or "iziet":              # ja lietotājs ieraksta stop vai iziet tad 
            #print("Programmas beigas")
            break
        
        
skaitlis1 = input("Ievadi 1. veselo skaitli")
skaitlis2 = input("Ievadi 2. veselo skaitli")

        
    
    


        
        
        
        
 
 
 
 
 



    

    
    
    
