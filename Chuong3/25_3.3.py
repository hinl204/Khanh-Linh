x=float(input("x="))
y=float(input("y="))
ch=str(input(""))

if ch=="+":
    print("Phep toan:+\n" + str(x)+ "+" + str(y) + "=",(x+y))
elif ch=="-":
    print("Phep toan:-\n" + str(x)+ "-" + str(y) + "=",(x-y))
elif ch=="*":
    print("Phep toan:*\n" + str(x)+ "*" + str(y) + "=",(x*y))
elif ch=="/":
    print("Phep toan:/\n" + str(x)+ "/" + str(y) + "=",(x/y))
elif x/y and y==0:
    print("Khong hop le",y=0)
else:
    print("Khong hop le")