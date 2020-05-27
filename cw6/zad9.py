import numpy as np


def zad9(n):
    # funkcja wewnętrzna
    def fibo(n):
        if n == 0:
            return []
        elif n == 1:
            return [1]
        elif n == 2:
            return [1, 1]
        else:
            fibos = [1, 1]
            for indeks in range(n-2):
                fibos.append(fibos[-1] + fibos[-2])
            return fibos
    # print(fibo(n))
    # teraz Numpy array
    import math as m
    shape = int(m.sqrt(n))
    return np.array(fibo(n)).reshape((shape, shape))

print(zad9(4))