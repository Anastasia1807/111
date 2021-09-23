from math import *
a=float(input("Enter side a: "))
b=float(input("Enter side b: "))
c=float(input("Enter side c: "))

p= (a+b+c)/2

S= sqrt(p*(p-a)*(p-b)*(p-c))

S= pow(p*(p-a)*(p-b)*(p-c), 0.5)

S= (p*(p-a)*(p-b)*(p-c))**0.5
print("S=",S)

