k=int(input("Nhập số k: "))
print('Các số Palindron nhỏ hơn k là: ')
for n in range(10,k+1):
	tmp=n
	tong=0
	while(n>0):
		r=n%10
		tong=(tong*10)+r
		n=int(n/10)
	if(tmp==tong):
		print(tmp)
