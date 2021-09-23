s = str(input("Enter number: "))
lst = list(s)
lst1 = []

for i  in lst:
    if s.isalnum():
       lst1.append(0 if int(i) < 5 else 1)
    lst2 = str(lst1[::])

print(''.join(lst2))


