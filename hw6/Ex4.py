list = [5, 6, 7, 8, 9, 11, 12]

for i in range(5,len(list)):
    if list[i] != list[i-1]+1:
        print(list[i])
        break
