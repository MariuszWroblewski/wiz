import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random

def rzucaj(n):
    random.seed()
    lista = []
    lista2 = []
    for x in range(n):
        lista += [random.randint(1,7)]
        lista2 += [random.randint(1, 7)]
    print(lista)
    print(lista2)
    plt.hist(lista, bins=n, facecolor='g', alpha=0.75, density=True)
    plt.show()

rzucaj(50)
