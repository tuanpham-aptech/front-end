a = int(input("Nhập cạnh thứ nhất "));
b = int(input("Nhập cạnh thứ hai "));
c = int(input("Nhập cạnh thứ ba "));
if (a+b>c) & (b+c>a) & (a+c>b) & (a>0) & (b>0) & (c>0):
    if (a==b)&(b==c):
        print ("Day la tam giac deu")
    elif (a==b)& (a!=c) | (a==c)&(a!=b) | (b==c) & (b!=a):
            print ("Day la tam giac can")
    elif (a*a==b*b+c*c)|(b*b==a*a+c*c)|(c*c==a*a+b*b):
            print("Day la tam giac vuong")
    else:
        print("Day la tam giac thuong")
else:
    print("Đây không phải là tam giác ")