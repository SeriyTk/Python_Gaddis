def add(birthdays):
    name = input('Введите имя: ')
    bday = input('Введите день рождения: ')
    if name not in birthdays: birthdays[name] = bday
    else: print('Этa запись уже существует.')