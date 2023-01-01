def Day_of_the_week():
    while True:
        number = int(input('Введите число от 1 до 7: '))
        if number <1 or number >7:
            print('Число не корректное.')
        else:
            if number == 1: print('Понедельник.'); break
            elif number == 2: print('Вторник'); break
            elif number == 3: print('Среда'); break
            elif number == 4: print('Четверг'); break
            elif number == 5: print('Пятница'); break
            elif number == 6: print('Суббота'); break
            else: print('Воскресенье'); break

Day_of_the_week()