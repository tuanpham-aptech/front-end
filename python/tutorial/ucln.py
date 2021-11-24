def ucln(a,b):
    x,y = abs(a),abs(b);
    while x!=y:
        if(x>y):
            x-=y;
        else:
            y-=x;
    return x;
kq = ucln(8,4);
btnn = (8*4)/kq;
print("Ước chung lớn nhất của a và b là : ",kq);
print("Bội chung nhỏ nhất của a và b là : ",btnn);
