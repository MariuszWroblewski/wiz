import math

liczba = float(input('podaj liczbę rzeczywistą >0: '))
try:
    wynik = math.sqrt(liczba)
    for i in range(0, len(str(liczba)), 1):
        print()
    print('Pierwsiastek z liczby: ',str(liczba) + ' = ' + str(wynik))
except ValueError:
    print('Nie można obliczyć pierwiastka z liczby <0 ')