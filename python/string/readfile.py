
#doc file text dem so dong, sô tu cua tep
f = open('E:/frontend/python/string/text.txt', "r",encoding = "utf-8")

luu = []
for line in f:
    luu.append(line.strip())
f.close()


f = open('E:/frontend/python/string/newtext.txt', "w",encoding = "utf-8")
for line in luu:
    f.write(line+"\n")
f.close()
# đếm số từ 
k=f.split()
print(k)
