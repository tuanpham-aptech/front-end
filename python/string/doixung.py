# a = input("Nhập xau kiểm tra ")
# k=0
# for i in range(0,len(a)):
#     for j in range(int(len(a)),int(len(a)/2),-1):
#         if i==j:
#             k+=1
# if(k==len(a)/2):
#     print("Chuỗi đối xứng ")
# else:
#     print("Chuỗi không đối xứng ")
def DoiXung(s):
    rs=True
    n = len(s)
    i=0
    while (i<n/2):
        if s[i]!=s[n-i-1]:
            rs=False
            break
        i=i+1
    return rs
DoiXung("abba")
 
      
