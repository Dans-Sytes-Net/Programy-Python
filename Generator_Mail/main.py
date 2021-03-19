import random

global domeny


def generuj_jeden(imie , nazwisko , rok_ur):
    index = random.randint(0,len(domeny)-1) # dostaniemy index
    return (nazwisko.lower() + "." + imie[0].lower() + str(rok_ur)[2:] + "@" +domeny[index])

def generuj(imie,nazwisko ,rok_ur):
    lista_mail = []
    for i in domeny:
        lista_mail.append(nazwisko.lower()+"."+imie[0].lower()+str(rok_ur)[2:]+"@"+i)
        lista_mail.append(imie[0].lower()+"."+nazwisko.lower()+str(rok_ur)[2:]+"@"+i)
    return  lista_mail

domeny= ["gmail.com","wp.pl","onet.pl"]
nazwisko = str(input("Podaj Nazwisko: "))
imie = str(input("Podaj Imie: "))
rok = int(input("Podaj rok urodzenia: "))
#print(generuj(imie,nazwisko,rok))
print(generuj_jeden(imie,nazwisko,rok))