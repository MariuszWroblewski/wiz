import numpy as np


def generuj2(n):
    a= np.arange(n,0,-1)
    print(a)
    mac = np.diag([n for n in range(n,0,-1)])
    print(mac)

generuj2(10)