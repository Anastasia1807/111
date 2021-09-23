v1 = int(input("Enter first volume of water in liters: "))
t1 = int(input("Enter first temperature  of water: "))
v2 = int(input("Enter second volume of water in liters: "))
t2 = int(input("Enter second temperature  of water: "))
x = (v1*t1+v2*t2)/(v1+v2)
v= v1+v2
print("volume and temperature the resulting mixture", v,",", x)
