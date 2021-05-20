import pandas as pd

plik = pd.ExcelFile("imiona.xlsx")
df = pd.read_excel(plik)
print(df)
