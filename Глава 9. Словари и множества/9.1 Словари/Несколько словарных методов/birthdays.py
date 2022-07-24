def display_menu():
    print('Друзья и их дни рождения')
    print('--------------------------------')
    print('''
1. Добавить новый день рождения.
2. Отыскать день рождения.
3. Изменить день рождения.
4. Удалить день рождения.
5. Выйти из программы.
    ''')

def add(birthdays):
    while True:
        name = input('Какое имя хотите внести: ')
        if name in birthdays: print('Этa запись уже существует.')
        else:
            if name == '': print('Данные занесены.'); break
            else: bday = input('Введите день рождения: '); birthdays[name] = bday

def look_up(birthdays):
    name = input('Какое имя хотите найти: ')
    print(birthdays.get(name, 'Не найдено.'))

def change(birthdays):
    name = input('Чьи данные хотите изменить: ')
    if name in birthdays: bday = input ('Введите новый день рождения: '); birthdays[name] = bday
    else: print (f'Имя{name} не найдено. ')

def delete(birthdays):
    name = input('Кого хотите удалить: ')
    if name in birthdays: del birthdays[name]; print(f'Имя {name} удалено.')
    else: print ('Это имя не найдено.')

