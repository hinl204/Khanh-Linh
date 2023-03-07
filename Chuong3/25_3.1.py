a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
p=(a+b+c)/2
square=int
import math
       
if a+b>c and b+c>a and a+c>b:
    square=round(math.sqrt(p*(p-a)*(p-b)*(p-c)),3)
    print("Dien tich=", square)     

else:
    print