import pandas as pd
import numpy as np
import xlrd


df = pd.read_excel('imiona.xlsx')
df2 = pd.DataFrame(df, columns=['Rok',  'Imie',  'Liczba',
                                'Plec'])

print(df)
