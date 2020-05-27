import numpy as np


a = np.arange(12)
b = a.reshape(3,4)
c = a.reshape(4,3)
print("Wektor a")
print(a)

print("3x4")
print(b)
print("spłaszczenie 3x4")
print(b.ravel())

print("4x3")
c = a.reshape(4,3)