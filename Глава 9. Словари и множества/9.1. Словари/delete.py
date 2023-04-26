def delete(birthdays):
    name = input('Введите имя: ')
    if name in birthdays: del birthdays[name]
    else: print ('Это имя не найдено.')