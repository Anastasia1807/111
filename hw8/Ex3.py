s = str(input(" Enter your nane and surname: "))
s1 = s.split(" ")
s2 = list(str(s1[0]))
s3 = list(str(s1[1]))


if s.replace(' ', '').isalpha() and len(s1)==2:
    print(s2[0] + '.', s3[0] + '.')
else:
    print('Data entered incorrectly')


# проверка на отсутствие цифр s.replace(' ', '').isalpha()
# проверка на количество введенных слов lst= [s.split(' ')]
# len(lst)>2, данные введены не корректно

