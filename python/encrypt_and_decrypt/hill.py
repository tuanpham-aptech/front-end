from cryptography.fernet import Fernet

key = Fernet.generate_key()

F= Fernet(key)
data = F.encrypt(b"Hello my name is Tuan pham,this is mobile number 0379679502")
print("Chuỗi sau mã hoá như sau --------------------------------:")
print(data)
#giải mã 
print("Chuỗi giải mã --------------------------")
print(F.decrypt(data))
