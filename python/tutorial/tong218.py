n = int( input(" nhap vao mot so "))

c, s, b =0,0, n
while b!=0:
    print(b%10)
    s=s+ b%10
    b= int(b/10)
    c=c+1

if s%c==0:
    print(n," la so dep");
else:
    print(n," la so khong dep");





