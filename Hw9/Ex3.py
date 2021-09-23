lst = [1, -5, 8, -9, -7, 3, 4, 5, 6]
lst1 = []

for x in lst:
    if x < 0:
        lst1.append(x)
a = sum(lst1)/len(lst1)
b = lst1.index(min(lst))
lst[b] = a
print(lst)