import numpy as np


a = np.arange(81).reshape(9,9)
print(a)
print(a.shape)
b = a.ravel()
print(b)
print(b.shape)
c = a.reshape(81,1)
print(c)
print(c.shape)
d = a.reshape(81,1)
print(d)
print(d.shape)