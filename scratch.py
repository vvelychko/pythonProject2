class Chislo:
    def __init__(self, x=0):
        self.x = x

    def __str__(self):
        return "{0}".format(self.x)

    def __add__(self, other):
        x = self.x + other.x
        return Chislo(x)

    def __sub__(self, other):
        x = self.x - other.x
        return Chislo(x)

    def __mul__(self, other):
        x = self.x * other.x
        return Chislo(x)

    def __truediv__(self, other):
        x = self.x / other.x
        return Chislo(x)


p1 = Chislo(1)
p2 = Chislo(2)
#1
print(p1+p2)
print(p1-p2)
print(p1*p2)
print(p1/p2)