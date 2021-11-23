class Phanso:
    def __init__(self):
        self.tu = 0
        self.mau = 0
    def nhap(seft):
        self.tu = int(input('Nhập tử số = '))
        self.mau = int(input('Nhập mẫu số = '))
    def xuat(seft):
        print("Tử số ",self.tu)
        print("Mẫu số ",self.mau)
    def __add__(self, other):
        tus = self.tu+other.tu
        maus = self.mau+other.mau
        return Phanso(tus,maus)

h = Phanso()