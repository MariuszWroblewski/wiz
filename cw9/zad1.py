import pandas as pd
import matplotlib.pyplot as plt


xlsx = pd.ExcelFile('imiona.xlsx')
maniek = pd.read_excel(xlsx)
df = pd.DataFrame(maniek, columns=['Rok',  'Imie', 'Liczba', 'Plec'])
print(df)
grupa = df.groupby(['Rok']).agg({'Liczba':['sum']})
print(grupa)
wykres = grupa.plot()
wykres.legend(['Liczba urodzeń'])
plt.show()
