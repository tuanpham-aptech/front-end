# for i in range(1,10):
# 	for j in range(0,10):
# 		for l in range(0,10):
# 			if (i*100+j*10+l==pow(i,3)+pow(j,3)+pow(l,3)):
# 				print('Số có ba chữ số có tổng lập phương bằng chính nó là: '+str(i)+str(j)+str(l))
for x in range(1, 20):
    for y in range(1, 33):
        for z in range(3, 100):
            if((x+y+z == 100) & (x*5 + y*3 + z/3 == 100)) :
                print("kết quả:  ")
                print("Trâu đứng:  ",x)
                print("Trâu nằm:  ",y)
                print("Trâu già ",z)