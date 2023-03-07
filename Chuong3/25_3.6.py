# Nhập vào 3 số thực a, b và c
a = float(input("Nhập số thực a: "))
b = float(input("Nhập số thực b: "))
c = float(input("Nhập số thực c: "))

# Kiểm tra 3 số trên có tạo thành tam giác hay không
if (a + b > c) and (a + c > b) and (b + c > a) and (a > 0) and (b > 0) and (c > 0):
    # Nếu là tam giác, kiểm tra loại tam giác
    if a == b == c:
        print("Tam giác đều")
    elif (a*a == b*b + c*c) or (b*b == a*a + c*c) or (c*c == a*a + b*b):
        print("Tam giác vuông")
    else:
        print("Tam giác loại khác")
else:
    print("Không hợp lệ")