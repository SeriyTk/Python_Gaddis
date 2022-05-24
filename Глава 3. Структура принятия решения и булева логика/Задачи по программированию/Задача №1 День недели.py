def Day_week():
    while True:
        num = int(input('Введите число от 1 до 7: '))
        if num <= 1 or num >=7: print('Число не корректное')
        else:
            if num == 1: print('Понедельник')
            elif num == 2: print("Вторник")
            elif num == 3: print("Среда")
            elif num == 4: print("Четверг")
            elif num == 5: print("Пятница")
            elif num == 6: print("Суббота")
            else: print("Воскресенье")

            break








Day_week()