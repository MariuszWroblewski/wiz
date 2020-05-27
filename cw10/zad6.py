import pandas as pd
import matplotlib.pyplot as plt


dane = pd.read_excel('imiona.xlsx')
df = pd.DataFrame(dane, columns=['Rok',  'Imie', 'Liczba', 'Plec'])
grupa = df.groupby(['Plec']).agg({'Plec': ['count']})
print(grupa)
wykres = grupa.plot.bar()

grupa2 = df.groupby(['Rok']).agg({'Liczba': ['sum']})
print(grupa2)
wykres2 = grupa2.plot()
plt.show()
