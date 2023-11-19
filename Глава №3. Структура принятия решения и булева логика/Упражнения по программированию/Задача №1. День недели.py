def Day_week():
    num = int(input('Введите число от 1 до 7: '))
    if num < 1 or num > 7: print('Число неправильное.')
    elif num == 1: print('Понедельник.')
    elif num == 2: print('Вторник.')
    elif num == 3: print('Среда.')
    elif num == 4: print('Четверг.')
    elif num == 5: print('Пятница.')
    elif num == 6: print('Суббота.')
    else: print('Воскресенье.')


if __name__ == '__main__': Day_week = Day_week()
