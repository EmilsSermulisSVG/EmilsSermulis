# 1. UZDEVUMS
# A klase ar ar atribūtiem
class Product(): #Abstraktā klase
    def __init__(self,name,price,quantity): #Bāzes klase ar laukiem
        self.name= name
        self.price=price
        self.quantity=quantity

# B metode lai apreķinātu kopējo cenu produktam
    def get_total_price(self):
        print(f"{self.name} ir tik daudz - {self.quantity}, 1 maksā tik daudz - {self.price}, kopējais maksā ir tik daudz - {self.quantity * self.price}")

# C - 2 objekti šai klasi kuri izsauc get_total_price

produkts1 = Product("siers",2,100)
produkts1.get_total_price()

produkts2 = Product("maize",2,145)
produkts2.get_total_price()

# 2 UZDEVUMS
# D klase ShoppingCart 
class ShoppingCart(Product):
    def __init__(self,name,price,quantity):
        super().__init__(name,price,quantity)

# E - metodes
    def add_product_to_cart(self):
        print(f"{self.name} pievientos grozam")
    def remove_product_from_cart(self):
        print(f"{self.name} ir izņemts no groza")
    def get_total_price(self):
        return super().get_total_price()

#F Iepirkuma groza objekts
shoppingcart = ShoppingCart("siers",2,1)
shoppingcart.add_product_to_cart()
shoppingcart.remove_product_from_cart()
shoppingcart.get_total_price()










