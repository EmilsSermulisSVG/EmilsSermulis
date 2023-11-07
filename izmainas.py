
saraksts = [2,6,8,3,8,1,6,3,9]
saraksts.append("Cepums")  #ar append pievieno beigās
print(saraksts)

# izmet no beigām
saraksts.pop()              # izmet 1 no beigām
print(saraksts)


saraksts.insert(3,"hello!")  # ievieto 3. no kreisās
print(saraksts)

saraksts.remove("hello!")      # izdēš norādīto vērtību
print(saraksts)

print("-------------------------")

tests = [1,2,3,4,5,6,7,8]       # izdzēš 1 elementu
del tests [2]
print(tests)

del tests [3:6]
print(tests)                    # izdzēš intervālu


print("-------------------------")


cipari = [1,2,3,4,5,6,7,8]
del cipari[2:7  :2]               # no 2-7 elementam dzēš ārā katru atro
print(cipari)

