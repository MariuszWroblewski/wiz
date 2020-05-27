import numpy as np
from math import sin

a = np.arange(6).reshape(2, 3)
print(a)
for element in a.flat:
    element *= np.sin(element)
print(a)
