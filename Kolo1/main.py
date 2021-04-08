# Z 1
import math
licznik = math.sqrt(6+(4*math.sqrt(14)))
print(round(math.pow((licznik/3),2)+math.cos(56)**2,2))

ln = math.log(35+math.e**4)
print(round(math.pow(ln,1/5),2))


# Z 2
plik = open("kolokwium.txt","r")
tekst = plik.read()
plik.close()
male = 0
duze = 0
for i in tekst[len(tekst)-20:]:
    if i.islower():
        male+=1
print("Male: ",male)
for i in tekst[:20]:
    if i.isupper():
        duze+=1
if duze!=0:
    print("Duze: ",duze)
else:
    print("Brak duzych")

# Z 3

lista = [1,2,3,4,5]
def sprawdz_ile_parzystych(lista):
    ile_parzystych = 0
    for i in range(len(lista)):
        if lista[i]%2==0:
            ile_parzystych=ile_parzystych+1
    print(ile_parzystych)

sprawdz_ile_parzystych(lista)

# Z 4

lista = ["informatyka", "kolokwium","kwiecien"]
for i in range(len(lista)):
    lista[i]=len(lista[i])
print(lista)

#Z 5

def fun(n):
    if n <=1: return 1
    return fun(n-1)*n

n = int(input("Podaj n: "))
print("Silnia =",fun(n))
