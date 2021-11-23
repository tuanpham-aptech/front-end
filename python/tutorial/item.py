# a=int(input("Nhập vào một số a:"))
# b = int(input("Nhập vào một số b:"))
# if a==0:
#     if b==0:
#         print('Phương trình vô số nghiệm')
#     else:
#         print('Phương trinh vo nghiem')
# else:
#     print('Phương trình có nghiệm ',-b/a)
# Số chính phương 
# a = int(input("Nhập số kiểm tra: "))
# if sqrt(a*a) == a:
#      print("Số vừa nhập  ",a,"là số chính phương")
# else:
#     print("Số vừa nhập  ",a,"không phải số chính phương")
 
# print("Nhập vào số N lớn hơn 0: ")
 
# n = int(input())
# check = False
 
# for i in range(1, n + 1 ):
#     if (i**2 == n):
#         check = True
#         break
 
# if (check == True):
#     print(n, " là số chính phương")
# else:
#     print(n, " không phải là số chính phương")
# import math
# a=int(input("Nhập vào một số a:"))
# b=int(input("Nhập vào một số b:"))
# c=int(input("Nhập vào một số c:"))
# if a==0:
#     if b==0:
#         print("Phương trình vô nghiệm ")
#     else:
#         print("Phương trình có nghiệm ",-c/b)
# else:
#     delta = b*b - 4*a*c
#     if delta >0:
#             x1 = (float)((-b + math.sqrt(delta)) / (2 * a))
#             x2 = (float)((-b - math.sqrt(delta)) / (2 * a))
#             print("Nghiệm thứ nhất là ",x1,"\nNghiệm thứ 2 là ",x2)
#     elif delta ==0:
#         print("Phương trình có nghiệm kép ",-b/(2*a))
#     else:
#         print("Phương trình vô nghiệm ")
#BÀI 1 
# tong = 0
# n = 0
 
# print("Hãy nhập vào số n: ")
# n = int(input())
 
# for i in range(1, n + 1) :
#     tong += 1 / i
 
# print("Tổng số là: ", tong)
#BÀI 2 
# def check_prime_number(n):
#     flag = 1;
#     if (n <2):
#         flag = 0
#         return flag 
    
#     for p in range(2, n):
#         if n % p == 0:
#             flag = 0
#             break 
#     return flag
# n = int(input(">> nhap so tu nhien: "))

# check = check_prime_number(n);
 
# if check == 1:
#     print(n," la so nguyen to")
# else:
#     print(n,"khong phai so nguyen to")
# a = int(input("Nhập số a : "));
# b = int(input("Nhập số b : "));
def uscln(a, b):
    temp1 = a;
    temp2 = b;
    while (temp1 != temp2):
        if (temp1 > temp2):
            temp1 -= temp2;
        else:
            temp2 -= temp1;
    uscln = temp1;
    return uscln;

def bscnn(a, b):
    return int((a * b) / uscln(a, b));
 
a = int(input("Nhập số nguyên dương a = "));
b = int(input("Nhập số nguyên dương b = "));
#tính USCLN của a và b
print("Ước số chung lớn nhất của", a, "và", b, "là:", uscln(a, b));
#tính BSCNN của a và b
print("Bội số chung nhỏ nhất của", a, "và", b, "là:", bscnn(a, b));