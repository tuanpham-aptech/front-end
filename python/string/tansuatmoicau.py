f = open("E:/frontend/python/string/text.txt", "r",encoding = "utf-8")
Linenb = dict({})
for line in f:
    if line.strip()=="":
        continue
    i=0
    for word in line.split():
        i=i+1
    if i not in Linenb:
        Linenb.update({i:1})
    else:
        Linenb[i] = Linenb[i]  + 1
f.close()
print("Độ dài dòng: Số lần")
for key in Linenb:
    print(key," : ",Linenb[key])
