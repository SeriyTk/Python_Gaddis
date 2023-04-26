def look_up(birthdays):
    name = input('Введите имя: ')
    print(birthdays.get(name, 'Не найдено.'))