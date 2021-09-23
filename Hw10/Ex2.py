#Напишите программу, которая принимает два набора и выводит все элементы первого, которых нет во втором.
l1 = set(input("Enter first set of numbers: "))
l2 = set(input("Enter second set of numbers: "))
print(l1.difference(l2))
