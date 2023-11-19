def Wheel_colors():
    numer = int(input('Введите номер кармана: '))
    if 1 > numer or numer > 36: print('Ошибка.')
    elif numer == 0: print('зеленый')
    elif 1 <= numer <= 10:
        if (numer == 1 or numer == 3 or numer == 5 or
                numer == 7 or numer == 9): print('красный')
        else: print('черный')
    elif 11 <= numer <= 18:
        if (numer == 11 or numer == 13 or numer == 15 or
                numer == 17 or numer == 19): print('черный')
        else: print('красный')
    elif 19 <= numer <= 28:
        if (numer == 19 or numer == 21 or numer == 23 or
                numer == 25 or numer == 27): print('красный')
        else: print('черный')
    elif 29 <= numer <= 36:
        if (numer == 29 or numer == 31 or numer == 33 or numer == 35): print('черный')
        else: print('красный')


if __name__ == '__main__': Wheel_colors = Wheel_colors()
