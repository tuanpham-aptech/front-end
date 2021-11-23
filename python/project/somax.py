print("Nhap vao so phan tu: ")
n=int(input())
lap=range(0,n,1)
ds=[]
for x in lap:
    print("Nhap gia tri phan tu thu ",x,"=")
    gt=int(input())
    ds.append(gt)
#b
max=ds[0]
for x in ds:
    if(x>max):
        max=x
print("Gia tri max = ",max)