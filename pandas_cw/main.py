import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import openpyxl
import xlrd

df = pd.read_excel("ludnosc.xlsx")
#print(df['Kraj'].head(5))
#print(df['Kraj'].tail(5))
kraje_ponad_srednia_2006 = df[df[2006] > df[2006].mean()]
#print(kraje_ponad_srednia_2006)
#print(kraje_ponad_srednia_2006[{'Kraj', 2006}])
#top5 = kraje_ponad_srednia_2006.head(5)
#plt.pie(top5[2006],autopct="%.2f ", labels=top5['Kraj'])
#plt.legend(loc=7)
#plt.title("Top 5 populacji z tabeli ludnosc")
#plt.show()

wartosci = [30,60,1000]
kraje = ['Polska','Niemcy','Holandia']
color = ['b','r','y']
#plt.pie(wartosci,labels=kraje,colors=color)
#plt.show()

wartosci=[20,20,60]
color = ['k','k','y']
#plt.pie(wartosci,colors=color)
#plt.show()

plt.bar(wartosci,wartosci)
#plt.show()

wartosci = [7.1,35.6,23.5,33.8]
color = ["#f4a582",'#67001f',"#d6604d","#b2182b"]
plt.pie(wartosci,autopct="%.1f %%",colors=color)
plt.show()



doge_df = pd.read_csv("dogecoin_csv.csv",sep=',')
print(doge_df.keys())
doge_price = doge_df[{'date', 'price(USD)'}]
print(doge_price)
fig ,sub = plt.subplots(2)
sub[0].plot(doge_df['date'].tail(50),doge_df['generatedCoins'].tail(50) , color='orange',marker='.')
sub[0].set_title('Generated Coins')
plt.xticks(rotation=90)
sub[1].plot(doge_price['date'].tail(50),doge_price['price(USD)'].tail(50))
sub[1].set_title('Price USD')
sub[1].set
plt.grid()
plt.show()