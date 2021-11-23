print("Nhap vao so phan tu: ")
n=int(input())
lap=range(0,n,1)
ds=[]
for x in lap:
    print("Nhap gia tri phan tu thu ",x,"=")
    gt=int(input())
    ds.append(gt)
#b
print("Các phần tử chẵn của dãy là :")
for x in ds:
    if(x%2 ==0):
        print(x)

        

