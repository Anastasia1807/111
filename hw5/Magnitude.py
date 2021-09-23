a = int(input("Enter a: "))
b = int(input("Enter b: "))

if abs(a)>abs(b):
    print("The number", a, " has biger magnitude then", b)
elif abs(b)>abs(a):
    print("The number", b, " has biger magnitude then", a)
elif abs(a)==abs(b):
    print("The numbers have equal magnitude")
