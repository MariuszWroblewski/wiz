import pandas as pd
import numpy as np
import xlrd


df = pd.read_excel('imiona.xlsx')
df2 = pd.DataFrame(df, columns=['Rok',  'Imie',  'Liczba',
                                'Plec'])

# print(df)
# print(df[df['Liczba']>1000])
print(df[df['Imie'] == 'MARIUSZ'])
print(df.agg({'Liczba': ['sum']}))
print(df.agg({'Liczba': ['sum']} & 'Liczba'))
