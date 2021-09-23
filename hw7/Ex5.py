row_1 = int(input('Enter number 1: '))
row_2 = int(input('Enter number 2: '))
s= row_1+row_2

if row_1>row_2:
    print('row_1 is bigger than row_2')
elif row_1<row_2:
    print('row_2 is bigger than row_1')
else:
    print('|row_1|row_2|sum')
    print("|", row_1,"|",row_2,"|",s)


