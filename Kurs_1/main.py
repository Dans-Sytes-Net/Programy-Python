imie = "DANIEL"
nazwisko = "KUCHARSKI"

imie_i_nazwisko = imie.capitalize()+" "+nazwisko.capitalize()
print(imie_i_nazwisko)

imie_i_nazwisko="1"
print(imie_i_nazwisko)

if imie_i_nazwisko.isdecimal():
    print("TRUE")

# Haslo musi mieć conajmiej 3 duże litery, 2 małe i długość 6, 2 cyfry
def spr_haslo(haslo):
    ilosc_d =0
    ilosc_m =0
    ilosc_c =0
    #blad = "Haslo sie zgadza"
    if len(haslo) < 6:
        return "Za krótkie"
    for litera in haslo:
        if litera.isdigit():
            ilosc_c+=1
        if (litera.islower()):
            ilosc_m+=1
        else:
            ilosc_d+=1
    if(ilosc_d<3 or ilosc_m<2):
        return "Ilość dużych lub małych liter się nie zgadza"
    if ilosc_c<2:
        return "Ilość cyfr jest za mała"
    return "OK"


#haslo = str(input("Podaj Haslo "))

#poprawnosc = spr_haslo(haslo)
#print(poprawnosc)

slowo = "abcdef"
lista = [1,2,3,4,5,6,77]
print(len(slowo))
print(len(lista))

for element in lista:
    print(element, end=",")

print()
for index in range(len(lista)):
    print(lista[index], end=",")
print()
x = [element for element in lista]
print(x)

lista_2 = lista.copy()
print(lista_2)
list_copy = lista
print(list_copy)
