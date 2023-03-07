TieuThu=int(input("Tieu thu="))
gia1=550
gia2=750
gia3=950
gia4=1350


if TieuThu<=100:
    TienDien=TieuThu*gia1
elif TieuThu<=150:
    TienDien=100*gia1 + (TieuThu-100)*gia2
elif TieuThu<=200:
    TienDien=100*gia1 + 50*gia2 + (TieuThu-150)*gia3
else:
    TienDien=100*gia1 + 50*gia2 + 50*gia3 + (TieuThu-200)*gia4


PhaiTra = TienDien*1.1
print("Phai tra=",PhaiTra,sep="")