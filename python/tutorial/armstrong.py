print('Các số Armstrong từ 2 đến 4 chữ số là: ')
for n in range(10,10000):
    p = len(str(n))
    s = 0
    k = n
    d = 0
    while k>0:
        d = k%10
        s = s + (pow(d,p))
        k = int(k/10)
    if n == s:
        print(n)