import pickle_data
# Константа для имени файла.
FILENAME = 'cellphones.dat'



print('''Выберите действие:
1.Законсервировать объект
2.Расконсервировать объект
''')
choise = int(input(': '))
while choise != 1 and choise != 2:
    print('Неправильный ввод.')
    choise = int(input(': '))
if choise == 1:
    pickle_data.pickle_cellphone(FILENAME)
elif choise == 2:
    pickle_data.unplckle_cellphone(FILENAME)
