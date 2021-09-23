lst = ['sheep', 'sheep', 'sheep', 'wolf', 'sheep']
lst.reverse()
lst2 = ['shep', 'sheep', 'wolf']
lst2.reverse()

for i in lst:
    if lst.index('wolf') != 0:
        num_sheep = lst.index('wolf')
        print(f'Oi! Sheep number {num_sheep}! You are about to be eaten by a wolf!')
        break
    elif lst.index('wolf') == 0:
     print('Please, go away and stop eating my sheep!')
     break


