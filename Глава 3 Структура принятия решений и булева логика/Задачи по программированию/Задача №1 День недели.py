def Day_of_week():
    number = int(input('Введите число от 1 до 7: '))
    while 1 > number or number > 7:
        print("Число не корректное.")
        number = int(input('Введите число от 1 до 7: '))
    else:
        if number == 1:
            print('Понедельник.')
        elif number == 2:
            print('Вторник.')
        elif number == 3:
            print('Среда.')
        elif number == 4:
            print('Четверг.')
        elif number == 5:
            print('Пятница.')
        elif number == 6:
            print('Суббота.')
        elif number == 7:
            print("Воскресенье.")


Day_of_week()
