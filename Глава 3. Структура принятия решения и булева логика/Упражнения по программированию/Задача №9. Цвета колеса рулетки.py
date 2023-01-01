def Roulette_wheel_colors():
    while True:
        pocket_number = int(input('Номер кармана: '))
        if pocket_number < 0 or pocket_number > 36: print('Не правильный номер.')
        else:
            if 1 <= pocket_number <= 10:
                if pocket_number % 2 == 0: print('Черный'); break
                else: print('Красный'); break
            elif 11 <= pocket_number <= 18:
                if pocket_number % 2 == 0: print('Красный'); break
                else: print('Черный'); break
            elif 19 <= pocket_number <= 28:
                if pocket_number % 2 == 0: print('Черный'); break
                else: print('Красный'); break
            elif 29 <= pocket_number <= 36:
                if pocket_number % 2 == 0: print('Красный'); break
                else: print('Черный'); break
            else: print('Зеленый'); break

Roulette_wheel_colors()