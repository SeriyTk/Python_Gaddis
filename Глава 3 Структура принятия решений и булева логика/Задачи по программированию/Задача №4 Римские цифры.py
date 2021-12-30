def Roman_numerals():
    numer = int(input('Введите число от 1 до 10: '))
    while 1 > numer or numer > 10:
        print('Вы ввели не коректное число.')
        numer = int(input('Введите число от 1 до 10: '))
    else:
        if numer == 1:
            print('I')
        elif numer == 2:
            print('II')
        elif numer == 3:
            print('III')
        elif numer == 4:
            print('IV')
        elif numer == 5:
            print('V')
        elif numer == 6:
            print('VI')
        elif numer == 7:
            print('VII')
        elif numer == 8:
            print('VIII')
        elif numer == 9:
            print('IX')
        else:
            print('X')

Roman_numerals()
