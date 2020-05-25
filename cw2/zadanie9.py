x = input("podaj liczbe wielocyfrowa:")
z = len(x)
wynik = 0
while (z > 0):
    wynik = wynik + int(x[z - 1])
    z = z - 1
    continue
print(wynik)