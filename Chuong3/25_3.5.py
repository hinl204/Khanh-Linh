# Nhập số ngày nghỉ của nhân viên
so_ngay_nghi = int(input("Nhập số ngày nghỉ của nhân viên: "))

# Xếp loại nhân viên dựa vào số ngày nghỉ
if so_ngay_nghi == 0:
    print("Xếp loại A")
elif so_ngay_nghi < 2:
    print("Xếp loại B")
elif so_ngay_nghi < 4:
    print("Xếp loại C")
else:
    print("Xếp loại D")