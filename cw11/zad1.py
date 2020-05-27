from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random


fig = plt.figure()
ax = fig.gca( projection = '3d' )

z = np.linspace( 0 , 2 * np.pi)
x = np.sin(z)
y = np.cos(z)
ax.plot(x, y, z, label = 'zadanie 1' )
ax.legend()
plt.show()