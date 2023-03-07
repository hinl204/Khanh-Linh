S=int(input("S="))
M1=int(input("M1="))
M2=int(input("M2="))
M3=int(input("M3="))
if S<=100:
     TienDien=S*M1
elif S<=150:
     TienDien=100*M1+(S-100)*M2
elif S>=151:
     TienDien=100*M1+50*M2+(S-150)*M3
print("Phai tra=",TienDien,sep="")
     
