print("Nhap vao so phan tu: ")
n=int(input())
lap=range(0,n,1)
ds=[]
for x in lap:
    print("Nhap gia tri phan tu thu ",x,"=")
    gt=int(input())
    ds.append(gt)
#b
dsam = []
for x in ds:
    if(x<0):
        dsam.append(x)
max = dsam[0]
for i in dsam:
    if(i>max):
        max = i
print("Gia tri max = ",max)