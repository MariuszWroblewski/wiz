import numpy as np


def zad7(n):
    mat = np.diag([2 for _ in range(n)])
    for indeks in range(1, n):
        vec = [2+(2*indeks) for _ in range(n-indeks)]
        mat += np.diag(vec, indeks)
        mat += np.diag(vec, -indeks)
    print(mat)

zad7(3)