def Roulette_wheel_colors():
    pocket_number = int(input('Введите номер кармана от 1 до 36: '))
    while 0 > pocket_number or pocket_number > 36:
        print('Ошибка! Некорректное число.')
        pocket_number = int(input('Введите номер кармана от 1 до 36: '))
    else:
        if pocket_number == 0:
            print('Зеленый.')
        elif 1 <= pocket_number <= 10:
            if pocket_number % 2 != 0:
                print('Красный.')
            else:
                print("Черный.")
        elif 11 <= pocket_number <= 18:
            if pocket_number % 2 != 0:
                print('Черный.')
            else:
                print("Красный.")
        elif 19 <= pocket_number <= 28:
            if pocket_number % 2 != 0:
                print('Красный.')
            else:
                print("Черный.")
        elif 29 <= pocket_number <= 36:
            if pocket_number % 2 != 0:
                print('Черный.')
            else:
                print("Красный.")

Roulette_wheel_colors()
