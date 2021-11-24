import math
import numpy 


def KeyMatrix(Key,n):
    Matrix =list()
    for i in range(n):
        temp = []
        for j in range(n):
            temp.append(ord(Key[i*n+j])-97)
        Matrix.append(temp)
    if numpy.linalg.det(Matrix)==0:
        print("Invalid Key !")
        exit(None)
    return Matrix

def Multiply(X,Y):
    Y= list([ord(x)-97] for x in Y)
    result =numpy.zeros([len(Y),1],dtype=int)
    result = numpy.dot(X,Y)
    return result
def Hill_encrypt(Plain,Key,n):
    cipher = ''
    for i in range(0,len(Plain),n):
        temp = Multiply(Matrix,Plain[i:i+n])
        for x in range(n):
            cipher +=chr(temp[x][0]%26+97)
    return cipher 




if __name__ == '__main__':
    Key = ''.join(input("Key: ").lower().split())
    Plain = ''.join(input("Plaintext: ").lower().split())
    n = math.sqrt(len(Key))
    if n!=math.trunc(n) or n ==0:
        print ("Invalid key")
        exit(None)
    n = math.floor(n)
    for i in range(n-len(Plain)%n):
        Plain +='x'
    Matrix = KeyMatrix(Key,n)
    print(Matrix)
    print("Cipher Text :",Hill_encrypt(Plain,Matrix,n))