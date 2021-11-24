from main.QuanLyHH import QuanLyHH
 
# khởi tạo một đối tượng QuanLySinhVien để quản lý sinh viên
qlhh = QuanLyHH()
while (1==1):
    print("\nCHUONG TRINH QUAN LY HANG HOA PYTHON")
    print("*************************MENU**************************")
    print("**  1. Them hang hoa.                               **")
    print("**  2. Hien thi danh sach sinh vien.                 **")
    print("**  0. Thoat                                         **")
    print("*******************************************************")
     
    key = int(input("Nhap tuy chon: "))
    if (key == 1):
        print("\n1. Them hàng hoá .")
        qlsv.nhapSinhVien()
        print("\nThem hàng hoá thanh cong!")
    elif (key == 2):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n7. Hien thi danh sach sinh vien.")
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nSanh sach sinh vien trong!")