def TinhTong(n, x):
    s=0
    tu =1
    mau =1
    for i in range(l, n+1): 
        tu= tu*x 
        mau=mau *i 
        s=s+tu/mau
    return s
n = int( input("Nhap n: ")) 
x = int( input("Nhap x: "))
print("Tong = ", TinhTong(n,x))