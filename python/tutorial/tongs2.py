def Sums2(n):
    s=0
    i=1
    while(i<=n):
        s+=1/i
        i+=1;
    return s
n = int (input("Nhap n: "))
print("Tong s2 = ",Sums2(n),"\n")