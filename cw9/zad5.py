import pandas as pd
import matplotlib.pyplot as plt


maniek = pd.read_csv('zamowienia.csv', sep=';')
df = pd.DataFrame(maniek, columns=['Kraj', 'Sprzedawca', 'Data zamowienia', 'idZamowienia', 'Utarg'])
grupa = df.groupby(['Sprzedawca']).agg({'Data zamowienia': ['count']})
print(grupa)
wykres = grupa.plot.bar()
wykres.set_ylabel('Suma zamowien')
wykres.set_xlabel('sprzedawca')
wykres.legend(['Suma zamówien'])
plt.show()
