class hanghoa:
    def __init__(self):
        self.ma = ''
        self.gia=0
        self.soluong =0
    def nhap(self):
        self.ma = input("Nhập mã: ")
        self.gia = int(input("Nhập giá: "))
        self.soluong = int(input("Nhập số lượng :"))
    def xuat(self):
        print("Mã hàng hoá :",self.ma, "Giá : ",self.gia,"Số lượng : ",self.soluong)
    def sluongmax10(self):
        if (self.soluong <10):
            self.xuat()
a =[]
n = int(input("Nhập số lượng :"))
for i in range(n):
    hh = hanghoa()
    hh.nhap()
    a.append(hh)
for i in range(n):
    a[i].xuat()
hl = hanghoa()
hl.sluongmax10()



