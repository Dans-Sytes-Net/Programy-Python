import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import openpyxl
import xlrd

df = pd.read_excel("ludnosc.xlsx")
print(df[[{'Kraj',2006}] > df[2006].mean()])
#plt.bar(df['Kraj'].head(5),df[2006].head(5))
plt.show()