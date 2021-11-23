path="E:/frontend/python/string/text.txt"
f=open(path,'r',encoding="utf-8")
luu=[]
i=0
for line in f:
    luu.append(line.strip())
    for word in line.split():
        i=i+1
f.close()
print(len(luu))
luu.fin('tuân');

print(i)
path='E:/frontend/python/string/newtext.txt'
f=open(path,'w',encoding="utf-8")
for line in luu:
    f.write(line+"\n")
f.close()