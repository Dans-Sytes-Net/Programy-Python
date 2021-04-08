# Liczby doskonałe to takie, które są sumą swoich dzielników właściwych (https://en.wikipedia.org/wiki/ Perfect_number).
# Napisz program, który dla podanej liczby naturalnej sprawdza, czy jest ona liczbą doskonałą.

liczba = int(input("Podaj liczbe: "))
suma =0
for i in range(1,liczba):  # 1 - 6  1 < 6
    if liczba%i==0:
        suma+=i

if liczba==suma:
    print("Tak")
else:
    print("Nie")
