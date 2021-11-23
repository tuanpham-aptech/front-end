class Student:

     # thuộc tính đối tượng
     def __init__(self, masv, ten, tuoi):
        self.masv = masv
        self.ten = ten
        self.tuoi = tuoi

     # phương thức
     def masinhvien(self, muc):
        return "{} Mã sinh viên  {}".format(self.masv,muc)

     def tensinhvien(self):
        return "{} Tên sinh viên ".format(self.ten)

     def tuoisinhvien(self): 
        return "{} Tuổi sinh viên ".format(self.tuoi)

sv1 = Student("1","Tuân",19)
sv2 = Student("2","Long",21)
sv3 = Student("3","Phạm Huệ",18)

print(sv1.masinhvien("Sống xanh "))
print(sv2.tensinhvien())
