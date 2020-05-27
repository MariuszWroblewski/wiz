import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


x = np.arange(1,21,1)
y = 1/x
plt.plot(x, y, 'g:', x, y, 'g^', label='f(x) = 1/x')
plt.title("Wykres funkcji f(x) dla x [1,20]")
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axis([0, len(x), 0, 1])
plt.legend()
plt.show()

# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'r')
# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'o')