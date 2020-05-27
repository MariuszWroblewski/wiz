import pandas as pd
import matplotlib.pyplot as plt


xlsx = pd.ExcelFile('imiona.xlsx')
maniek = pd.read_excel(xlsx)
df = pd.DataFrame(maniek, columns=['Rok',  'Imie', 'Liczba', 'Plec'])
grupa = df.groupby(['Plec']).agg({'Plec':['count']})
print(grupa)
wykres = grupa.plot.bar()
wykres.set_ylabel('Liczba urodzeń')
wykres.set_xlabel('Płeć')
wykres.legend(['Suma urodzeń'])
plt.show()
