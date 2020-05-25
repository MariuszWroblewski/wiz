def suma(a1=1, ile=10, r=1):
    wynik=[x for x in range(1, ile+1, r)]
    a = sum(wynik)
    print(a)


suma(1, 2, 1)