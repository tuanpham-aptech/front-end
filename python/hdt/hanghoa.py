class Hanghoa:
    def __init__(self, id, name,quantity):
        self._id = id
        self._name = name
        self._quantity = quantity
    listHangHoa = []
    def nhapSinhVien(self):
        svId = int(input("Nhập mã hh: "))
        name = input("Nhap ten hh: ")
        quantity= int(input("Nhap số lượng : "))
        
        sv = HangHoa(svId, name,quantity)
        self.listHangHoa.append(sv)
    def showSinhVien(self, listHH):
        # hien thi tieu de cot
        print("{:<8} {:<18} {:<8} {:<8}{:<8} {:<8} {:<8} {:<8} {:<8}"
            .format("Mã hh ", "Tên ", "Số lượng "))
        # hien thi danh sach sinh vien
        if (listHH.__len__() > 0):
            for sv in listHH:
                print("{:<8} {:<18} {:<8} "
                    .format(sv._id, sv._name, sv._quantity))
    print("\n")

