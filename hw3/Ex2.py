from math import *

a=float(input("Enter cathetus a: "))
b=float(input("Enter cathetus b: "))

S=0.5*a*b

c=hypot(a,b)

P= a+b+c

print("Perimeter= ", P)
print("Square= ", S)