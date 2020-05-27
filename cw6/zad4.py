import numpy as np


def generuj(n,m):
    a = np.logspace(n,3, num=m)
    return a

a= generuj(2,3)
print(a)