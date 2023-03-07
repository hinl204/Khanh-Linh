# Nhập điểm thi 3 môn: Toán, Lý, Hoá
toan = float(input("Nhập điểm Toán: "))
ly = float(input("Nhập điểm Lý: "))
hoa = float(input("Nhập điểm Hóa: "))

# Tính điểm trung bình
diem_trung_binh = (toan * 2 + ly * 3 + hoa) / 6

# Xếp loại học sinh
if diem_trung_binh >= 9 and diem_trung_binh <= 10 :
    print("Học sinh xuất xắc")
elif diem_trung_binh >= 8 and diem_trung_binh <= 9:
    print("Học sinh giỏi")
elif diem_trung_binh >= 7 and diem_trung_binh <= 8:
    print("Học sinh khá")
elif diem_trung_binh >= 6 and diem_trung_binh <= 7:
    print("Học sinh trung bình khá")
elif diem_trung_binh >= 5 and diem_trung_binh <= 6:
    print("Học sinh trung bình")
elif diem_trung_binh >= 3 and diem_trung_binh <= 5:
    print("Học sinh yếu")
else:
    print("Học sinh kém")
