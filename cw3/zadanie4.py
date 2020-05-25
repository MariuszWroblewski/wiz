def mon(a):
    if a > 0:
        print('Funkcja jest rosnaca!')
    elif a < 0:
        print('Funkja jest malejąca!')
    else:
        print('Funkcja jest stała!')


a = int(input('Podaj współczynnik a funkcji liniowej: '))
mon(a)
