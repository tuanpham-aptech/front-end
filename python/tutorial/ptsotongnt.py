# a = int(input("Nhập số cần thực hiện "));
b = 0;
def ktnt(n):
    dem = 0;
   for const in range(1,n):
       if(n%const == 0):
           dem++;
if(dem == 2):
    return false;

for i in range(1,a):
    ktnt(i)== true;
    b+=i;
if(b > a):
    print("Tổng số nguyên tố của a là :",b);