print("Let's solve the equation ax+b=0")
a = int(input("Enter a:"))
b = int(input("Enter b:"))

x = None

if a==0:
    print("The equation has no solution")
elif b==0:
    print("x=0")
else:
    x = b * (-1) / a
print("x=",x)