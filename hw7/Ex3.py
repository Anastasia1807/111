lst = [1, 10, 12, 15, 6, -9, 48]
lst1 = []
d = '1,2,3,4,5,6,7'
i = 1
for i in lst:
    if lst[i]%int(d[:])== 0:
        lst1 = lst[i]
        print(lst1)
    i +=1