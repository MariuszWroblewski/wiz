import pandas as pd
import matplotlib.pyplot as plt


dane = pd.read_excel('imiona.xlsx')
df = pd.DataFrame(dane, columns=['Rok',  'Imie', 'Liczba', 'Plec'])
grupa = df.groupby(['Plec']).agg({'Plec':['count']})
print(grupa)
wykres = grupa.plot.pie(subplots=True, autopct='%1.1f%%')
plt.title('Procentowe urodzenia wzgledem płci z ostanich 5 lat')
maniek = ['Kobiety','Mężczyźni']
plt.legend(maniek)
plt.show()
