#Написать программу, которая на вход принимает список чисел и проверяет,
# все ли числа в этой последовательности уникальны

l = [1, 2, 3, 4, 5, 6, 7, 8, 8, 1, 9, 0, ]
s = set(l)
if len(l) == len(s):
    print("All numbers are unique")
else:
    print("Numbers are not unique")
