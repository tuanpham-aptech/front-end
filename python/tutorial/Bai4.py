import math
n = int(input(" nhap n "))

a = []
for i in range(2, n):
    nt = True
    for j in range(2, int(math.sqrt(i))+1):
        if i%j==0:
            nt=False
            break
    if  nt:
        # Thêm vào mảng 
        a.append(i)
c=0
def Duyet(a, kq, n, i):
    # Duyệt tổ hợp nhị phân 0 1 
    for j in range(2):
        # Tổ hợp thứ i gán bằng j
        kq[i]=j
        # Kiểm tra nếu i 
        if i==len(a)-1:
            s=0
            for k in range(len(a)):
                if kq[k] ==1:
                    s=s+a[k]
            if s==n:
                tem=""
                for k in range(len(a)):
                    if kq[k] ==1:
                        if tem =="":
                            tem = str(a[k])
                        else:
                            tem = tem +" + " +  str(a[k])
                global c
                c=c+1
                print(str(c)+"\t"+ tem+" = " + str(n))
        else:
            Duyet(a, kq, n, i+1)

kq=[]
for i in range(len(a)):
    kq.append(0)

Duyet(a, kq, n, 0)
'''
for i in a:
    print(i,"\t")
'''
#luu phuong an
'''
b=[]
i = n-1
x=n
while i!=0:
    while i not in a:
        i=i-1
    b.append(i)
    x=x-i
    i=x-1
    if i==0:
        b.append(x)

for i in b:
    print(i," + ")
'''

