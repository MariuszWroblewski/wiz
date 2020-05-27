import numpy as np

a = np.arange(2, dtype='float32')
print(a)
print(a.dtype)
b = a.astype('int64')
print(b)
print(b.dtype)