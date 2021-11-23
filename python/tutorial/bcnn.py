def uscln(a,b):
    x,y = abs(a),abs(b);
    while x!=y:
        if(x>y):
            x-=y;
        else:
            y-=x;
    return x;
def bscnn(a, b):
    return int((a * b) / uscln(a, b));
print("BNNN",bscnn(8,4));