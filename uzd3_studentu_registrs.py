class Students:
    def __init__(self,vards,uzvards,vecums,kursa_nr):
        self.vards = vards
        self.uzvards = uzvards
        self.vecums = vecums
        self.kursa_nr = kursa_nr
        
    def izvade(self):
        while True:
            try:
                if vecums >= 18:
                    print(f"\nStudents : {self.vards} {self.uzvards}\nVecums : {self.vecums}\nKurss : {self.kursa_nr}. kurss")
                    break
                elif vecums <18:
                    print("Nepareizi ievadīti dati")
                    break
                if kursa_nr > 4 or kursa_nr < 1:
                    print("nepareizi ievadīti dati")
                    break
            except ValueError:
                print("Ievadītas nepareizas vērtības")
                break
                
vards = input("Ievadiet jūsu vārdu: ")
uzvards = input("Ievadiet jūsu uzvārdu: ")
vecums = int(input("Ievadiet jūsu vecumu: "))
kursa_nr = int(input("Ievadiet jūsu kursa nummuru: "))

students = Students(vards,uzvards,vecums,kursa_nr)
students.izvade()

