# n = int(input("Nhập kích thước "));
# a = []
# for i in range(0,n):
#     b =[]
#     for j in range(0,n):
#         print("Nhập a[",i,"]","[",j,"]= ")
#         b = b+ [int(input())]
#     a = a+[b]
# print(a)
f = open("E:/frontend/python/string/matrix.txt", "r", encoding="utf-8")
n = int(f.readline())
a=[]
for l in f:
    b=[]
    ws= l.strip().split()
    if len(ws)<3:
        continue
    for j in range(n):
        b.append(int(ws[j]))
    a.append(b)
f.close()

for i in range(n):
    l=""
    for j in range(n):
        l= l+ str(a[i][j])+" \t "
    print(l,"\n")
    