# Napisz program wyświetlający na standardowym wyjściu (konsoli) liczby pomiędzy
# 100 a 200 podzielne przez 11 a niepodzielne przez 15.

for liczba in range(100,201):
    if liczba%11==0 and liczba%15!=0:
        print(liczba)