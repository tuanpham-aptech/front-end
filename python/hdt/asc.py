class hanghoa:
    def __init__(self):
        self.ma=""
        self.gia=0
        self.slg=0
    def xuat(self):
        print("Ma hang hoa: ",self.ma)
        print("Don gia: ",self.gia)
        print("So luong hang: ",self.slg)
    def nhap(self):
        self.ma = input("Nhap ma hang: ")
        self.gia = int(input("Nhap don gia: "))
        self.slg = int(input("Nhap so luong hang: "))
    def in10(self):
        if(self.slg<10):
            self.xuat()

class Maytinh(hanghoa):
    def __int__(self,cpu,ram):
        super(Maytinh,self).__int__(cpu,ram)
    def nhap(self):
        super(Maytinh,self).nhap()
        self.cpu = input("Nhap số cpu: ")
        self.ram = int(input("Nhap số ram: "))
    def xuat(self):
        super(Maytinh,self).xuat()
        print("Số cpu: ",self.cpu)
        print("Số ram: ",self.ram)

a=[]
n=int(input("So hang hoa can nhap: "))
for i in range(n):
    print("__________________")
    print("Hang hoa thu ",i+1)
    hang=Maytinh()
    hang.nhap()
    a.append(hang)
for i in range(n):
    print("Hang hoa co so luong > 10 la:")
    a[i].in10()
    print("________")