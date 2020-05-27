import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


x = np.arange(1,21,1)
y = 1/x
plt.plot(x, y, label='f(x) = 1/x')
plt.xlabel('os x')
plt.ylabel('os y')
plt.axis([0, len(x), 0, 1])
plt.legend()
plt.show()