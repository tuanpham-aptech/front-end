import math
import numpy 

from egcd import egcd

anphabet = 'abcdefghijklmnopqrstuvxwxyz'
letter_to_index = dict(anphabet,range(len(anphabet)))
index_to_letter = dict(zip(range(len(anphabet)),anphabet))
def matrix_mod_inv(matrix,modulus):
    det = int(np.round(np.linalg.det(matrix)))
    det_inv = egcd(det,modulus[1]%modulus)
    matrix_modules_inv = det_inv * np.round(det * np.linalg.inv(matrix)).estype(int)%modulus
    return matrix_modules_inv
def encrypt(message,K):
    encrypted =''
    message_in_numbers = []
    for letter in message:
        message_in_numbers.append(letter_to_index[letter])
    splt_P = [message_in_numbers[i:i+int(K.shape[0])] for i in range(0,len(message_in_numbers),int(K.shape[0]))]
    for P in split_P:
        P = np.transpose(np.asarray(P))[:,np.newaxis]
        while P.shape[0] != K.shape[0]:
            np.append(P,letter_to_index['x'])[:,np.newaxis]
        np.dot(K,P) % len(anphabet)
        n = numbers.shape[0]
        for idx in range(n):
            number = int(numbers[idx],0)
            encrypted += index_to_letter[number]
    return encrypted
    pass
def decrypt(cipher,Kinv):
    decrypted = ''
    cipher_in_numbers = []
    for letter in cipher:
        cipher_in_numbers.append(letter_to_index[letter])
    splt_C = [cipher_in_numbers[i:i+ int(Kinv.shape[0])] for i in range(0,len(cipher_in_numbers),int(Kinv.shape[0]))]

    for C in split_C:
        C = np.transpose(np.asarray(C))[:,np.newaxis]
    numbers = np.dot(Kinv,C)%len(anphabet)
    n = numbers.shape[0]
    for idx in range(n):
        number = int(numbers[idx,0])
        decrypted += index_to_letter[number]
    return decrypted
def main():
    K = np.array([[3,3],[2,5]])
    message = 'help'

    encrypted_message =encrypt(message,K)
    Kinv = matrix_modules_inv(K,len(anphabet))
    decrypted_message = decrypt(encrypted_message,Kinv)
    print("Chuỗi ban đầu "+message)
    print("Chuỗi mã hoá "+encrypted_message)
    print("Chuỗi giải mã "+decrypted_message)
main()

