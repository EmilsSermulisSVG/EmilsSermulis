# uztaisīt programmu kurā zemūdene spridzina burbuļus
#tiek skaitīti punkti

from random import *
from tkinter import *
from math import *

logs = Tk()
garums = 700
platums = 700
logs.title("Burbuļu spridzinātājs")
a = Canvas(logs, width= garums, height=platums, bg="lightblue")
a.pack()


kugis_id2 = a.create_oval(0,0,180,100,outline="black",width=10)



mainloop()