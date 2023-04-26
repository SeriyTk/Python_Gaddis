def change(birthdays):
    name = input('Введите имя: ')
    if name in birthdays: bday = input('Введите новый день рождения: '); birthdays[name] = bday
    else: print('Этo имя не найдено.')