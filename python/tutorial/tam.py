import math
# A(a,b)
a = int(input("Nhập số nguyên dương a = "));
b = int(input("Nhập số nguyên dương b = "));
# B(c,d);
c = int(input("Nhập số nguyên dương c = "));
d = int(input("Nhập số nguyên dương d = "));
# C(e,f);
e = int(input("Nhập số nguyên dương e = "));
f = int(input("Nhập số nguyên dương f = "));
AB = math.sqrt(((c-a)**2)+((d-b)**2))
AC = math.sqrt(((e-a)**2)+((f-b)**2))
BC = math.sqrt(((e-c)**2)+((f-d)**2))
p = (AB + AC + BC)/2
s = math.sqrt(p*(p-AB)*(p-AC)*(p-AC));
print("Diện tích tam giác là : s= ",s);
print("Chu vi tam giác ",(AB+AC+BC));





