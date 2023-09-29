cilveks = str(input("Tu esi students vai personāls :")) 
sanemNesanem = str(input("Vai tu esi nodevis visas grāmatas laikā? (jā\nē) : "))   
zurnali = str(input("Tu gribi izņemt žurnālus? (jā/nē)")) 
izdevumi = str(input("Tu gribi izņemt pieprasītos izdevumus vai grāmats (pieprasīto/grāmatas)")) 





if sanemNesanem == "jā" and cilveks == "students" and izdevumi == "pieprasīto" or "grāmatas" and zurnali == "jā":
    if izdevumi == "pieprasīto":
        print("Tu vari izņemt pieprasīto uz 2 dienām")
    elif izdevumi == "grāmatas":
        print("Tu vari izņemt grāmatas uz 14 dienām")
        print("tu vari žurnālus izņemt uz 7 dienām")


        
        
        
if  sanemNesanem == "jā" and cilveks == "personāls" and izdevumi == "pieprasīto" or "grāmatas" and zurnali == "jā":
     if izdevumi == "pieprasīto":
        print("Tu vari izņemt pieprasīto uz 2 dienām")
     elif izdevumi == "grāmatas":
        print("Tu vari izņemt grāmatas uz 28 dienām")
        print("tu vari žurnālus izņemt uz 7 dienām")

        