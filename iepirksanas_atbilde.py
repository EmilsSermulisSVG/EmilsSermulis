# 1. UZDEVUMS
# A klase ar atribūtiem
class Product(): #Abstraktā klase
    def __init__(self,name,price,quantity): #Bāzes klase ar laukiem
        self.name= name
        self.price=price
        self.quantity=quantity

# B metode lai apreķinātu kopējo cenu produktam
    def get_total_price(self):
        total_price = self.quantity * self.price
        return total_price

# C - 2 objekti šai klasi kuri izsauc get_total_price
siers = Product("siers",2,100)
print("Siers", siers.get_total_price())

maize = Product("maize",2,145)
print("Maize", maize.get_total_price())

#2. UZDEVUMS

#D klase ShoppingCart 
class ShoppingCart():

# E - metodes
    def add_product_to_cart(self,product,):
        print(product.name," pievientos grozam")
    def remove_product_from_cart(self,product):
        print(product.name,"ir izņemts no groza")
    def get_total_price(self,product):
        print(product.get_total_price,"Kopējā summa:")

#F Iepirkuma groza objekts
shoppingcart = ShoppingCart()

#G izsaukt metodes
shoppingcart.add_product_to_cart(siers)
shoppingcart.remove_product_from_cart(siers)
shoppingcart.get_total_price(siers)

#3. UZDEVUMS

#H klase SystemUser
class SystemUser():

#I atribūti 
    def __init__(self,username,password,email): 
        self.username= username
        self.password=password
        self.email=email

#J nomaina eksistējošos atribūtusa
    def set_user_info(self,newusername,newpassword,newemail):
        self.newusername= newusername
        self.newpassword=newpassword
        self.newemail=newemail
        print("Informācija ir nomainīta!")

    def get_user_name(self):
        print("Informācija par lietotāju---")
        print("Lietotājs:",self.username)
        print("Parole:",self.password)
        print("E-pasts:",self.email)

#K objektu izveide kur nomaina info
Liene = SystemUser("Liene","12345","liene@gmail.com")
#nomainit info un paradit
Liene.set_user_info("LieneSaule","54321","liene.saule@gmail.com")
Liene.get_user_name()

#4 UZDEVUMS

#L Manto
class Customer(SystemUser):
#N pievieno atribūtus
    def __init__(self,username,pasword,email,customer_id,purchase_history,membership_status):
        super().__init__(username,pasword,email)
        self.customer_id= customer_id
        self.purchase_history= purchase_history
        self.membership_status= membership_status

#M metožu pārrakstīšana
    def set_user_info(self,newusername,newpasword,newemail,newcustomer_id,newpurchase_history,newmembership_status):
        super().set_user_info(newusername,newpasword,newemail)
        self.newcustomer_id = newcustomer_id
        self.newpurchase_history = newpurchase_history
        self.newmembership_status = newmembership_status

    def get_user_info(self):
        super().get_user_info()
        print("Informācija par lietotāju---")
        print("Klienta ID:",self.newcustomer_id)
        print("Pirkumu vēsture:",self.newpurchase_history)
        print("Lojalitāte:",self.newmembership_status)

# O klienta objekts ar atjauninānātu informāiju

Karlis = Customer("karlis4","1234","karlis@gmail.com",13,"","")
#atjauninat info
Karlis.set_user_info("karlis5","42312","karlis@gmail.com",13,"Āboli","aaa")

Karlis.get_user_info