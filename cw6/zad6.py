import numpy as np

def zad6():
    # wyrazy jako wektory znaków (liter)
    malina = np.array(list('malina'))
    lizak = np.array(list('lizak'))
    jagoda = np.array(list('jagoda'))
    wykreslanka = np.empty((6, 6), dtype='str')
    wykreslanka[:, 0] = malina
    wykreslanka[2,:5] = lizak
    wykreslanka[5,::-1] = jagoda
    print(wykreslanka)

zad6()