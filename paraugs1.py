''' mainīgo tipu pārveidošana,
datu tipu iegūšana no literāra,
konkatenācija'''

name = "Anna"
teksts = "teksts"
skaitlis = 9 #int tips
print(name)

kombo = name, teksts #mainīgo apvienošana
print(kombo)

varda_garums = len(teksts)
print('Mainīgā garmus:',varda_garums)

a = b = c = 300 #chained_assigment = kaskādes veida piešķiršana
print(a,b,c)

x, y = 10, 'hello'
print(x)
print(y)