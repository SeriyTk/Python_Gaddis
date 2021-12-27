name1 = 'вася'
name2 = 'ваня'
if name1 > name2:
    print(f'Строка {name1} больше, чем строка {name2}.')
else:
    print(f'Строка {name2} больше, чем строка {name1}.')

print('--------------------------------------------------------')
def sort_names():
    name1 = input('Введите фамилию: ')
    name2 = input('Введите еще одну фамилию: ')
    if name1 < name2:
        print(name1)
        print(name2)
    else:
        print(name2)
        print(name1)

sort_names()