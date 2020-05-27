import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 30, 0.1)
s = np.sin(x)
s1 = np.sin(x)+2
plt.plot(x, s+2, label='sin(x)')
plt.plot(x, -s, label='sin(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title("Wykres sin(x) i cos(x)")
plt.axis([-1, 30, -1.0, 3.0])
plt.legend(loc="center left")
plt.show()