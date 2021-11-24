n = int( input("Nhap số phần tử mảng  ")) 
a = [];
for i in range(n):
    a.append(input('Nhap so thu %d: ' % (i+1)))

print(a)
for i in range(len(a)):
    print("Phần tử thứ %d",i+1,"là =", a[i])
