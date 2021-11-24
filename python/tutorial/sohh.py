def kthh(a):
    tong = 0
    for i in range(1, a):
        if (a % i == 0):
            tong += i
    
    if (tong == a):
        return True
    else:
        return False
n = int(input("Nhập số n "));
for i in range(n):
    if kthh(i)==True:
        print(i)