list = [1, 2, 3, 4, 5, 6 , 8, 12, 15, 21, 25]
number = int (input('Enter number: '))


for i in range(len(list)):
    if list[i]%number==0:
        print(list[i])
else:
    print("No multiples found")



