#doc file text dem so dong, sô tu cua tep
#dem so lan xuat hien cua tung tu

#bai tap: Tinh tần số các dòng theo do dai, ví dụ  co bao nhieu cau co do dai bang 1, 2, 3, 4, ....n
# Bài 2. Nhập vào từ tệp một ma trận các số nguyên gồm 4 hàng 4 cột (ma trận vuông cấp 4)

f = open("E:/Đề tài KC/test Giong Hang/VietTrung/Vietnamese_100_02.txt", "r",encoding = "utf-16")

'''
SoCau=0
SoTu=0

for line in f:
    if line.strip()=="":
        continue
    SoCau=SoCau+1
    SoTu= SoTu + len(line.split())

f.close()
print("So cau cua  tep: ", SoCau)
print("So tu cua  tep: ", SoTu)
'''

TuVung = dict({})
for line in f:
    if line.strip()=="":
        continue
    ws= line.split()
    for w in ws:
        if w not in TuVung:
            TuVung.update({w:1})
        else:
            TuVung[w] = TuVung[w]  + 1
f.close()

# TuVung_key = sorted(TuVung, key=TuVung.get, reverse=True) # sap xep giam dan theo gia tri

# f = open("E:/Đề tài KC/test Giong Hang/VietTrung/Vietnamese_100_02_TongKe.txt", "w",encoding = "utf-16")
# f.write("So tu "+ str(len(TuVung))+"\n")
# for w in TuVung_key:
#     f.write(w+"\t"+str(TuVung[w])+"\n")
# f.close()
