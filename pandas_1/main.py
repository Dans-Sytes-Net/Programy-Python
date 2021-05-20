import pandas as pd
import numpy as np

daty = pd.date_range('20180401', periods=3)
df = pd.DataFrame([[1,2,3,4,5]], index=[1,2,3,4,5])
#print(df)

data = {'Kraj': ['Belgia',  'Indie',  'Brazylia'],'Stolica': ['Bruksela',  'New Delhi',  'Brasilia'],'Populacja': [11190846, 1303171035, 207847528]}
df = pd.DataFrame(data, columns=['Kraj',  'Populacja',  'Stolica'])
print(df)
print(df['Stolica'])
print(df.loc[[0],  ['Kraj']])
print(df.head(1))
print(df.head(2))
print(df.tail(1))

print(df.T)  # Transpoozycja (zamiana kolumny z wierszem)

lista_osob = {'Imie':['Daniel' , 'Michal' , 'Marek'] , 'Nazwisko':['K' , 'M', 'T'] , 'Wiek':[22,31,25]}
#print(lista_osob.keys())
df = pd.DataFrame(lista_osob , columns=lista_osob.keys())
print(df.describe())
print('Srednia wiaku', df['Wiek'].mean())

szukaj = ['Marek', 'Adrian']
print(df.isin(szukaj))