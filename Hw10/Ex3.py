#Написать программу, которая на вход принимает список чисел и проверяет,
# все ли числа в этой последовательности уникальны

l = []

for _ in range(5) :
    l.append(int(input('Enter number: ')))
    s = set(l)
if len(l) == len(s):
    print("All numbers are unique")
else:
    print("Numbers are not unique")



