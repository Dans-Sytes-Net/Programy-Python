class Kwadrat:
    def __init__(self,a,b=0):
        self.a = a
        if b==0:
            self.zmien_na_kw()
        else:
            self.b = b

    def zmien_na_kw(self):
        self.b = self.a

    def pole(self):
        return  self.a*self.b

kwadrat = Kwadrat(5)
print(kwadrat.pole())
prostokat = Kwadrat(2,3)
print(prostokat.pole())
prostokat.zmien_na_kw()
print(prostokat.pole())
