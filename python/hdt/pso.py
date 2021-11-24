class Phanso:
    def __init__(self, a,b):
        self.a = a
        self.b = b
    def __add__(self, object2):
        x = self.a / object2.a
        y = self.b / object2.b
        return x+y
ps1 = Phanso(2,4)
ps2 = Phanso(3,6)
print(ps1 + ps2)