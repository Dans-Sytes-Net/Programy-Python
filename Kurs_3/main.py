class iter:
    def __init__(self, data):
        self.data = data
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.data):
            raise StopIteration
        self.index = self.index + 1
        list={'a','e','o','u','i','y'}
        if self.data[self.index] in list:
            return self.data[self.index]

ob = iter("Hello")
print(ob.__iter__())
print(ob.__next__())
print(ob.__next__())
print(ob.__next__())
print(ob.__next__())
print(ob.__next__())


class liczby:
    def __init__(self,poczatek,koniec,skok):
        self.poczatek = poczatek-skok
        self.koniec = koniec
        self.skok = skok

    def __iter__(self):
        return self

    def __next__(self):
        if self.poczatek >= self.koniec:
            raise StopIteration
        self.poczatek += self.skok
        return self.poczatek

print()
#licz1 = liczby(1,20,1)
#try:
#    for i in range(15):
#        print(licz1.__next__())
#except StopIteration:
#        print("STOP")

#lista = [x for x in range(100000000000)]
#print(lista)

def fib(ile):
    lista = [1, 1]
    for index in range(2, ile+2, 1):
        lista.append(lista[index-1] + lista[index-2])
        yield lista[index-2]

def sum_fib(n):
    n_fib = fib(n)
    suma = 0
    for i in range(n):
        suma+=next(n_fib)
    yield suma

print(next(sum_fib(10000000)))


def liczby2():
    i=0
    while 1:
        i+=1
        yield i

def suma(a,b):
    return a+b

print()
#licz2 = liczby2()
#for i in range(100):
#    print(suma(next(licz2),next(licz2)))

a = input("STOP")