def Roman_numerals():
    while True:
        number = int(input('Введите число от 1 до 10: '))
        if number < 1 or number > 10: print('Число некорректное')
        else:
            if number == 1: print('I')
            elif number ==2: print('II')
            elif number == 3: print('III')
            elif number == 4: print('IV')
            elif number == 5: print('V')
            elif number == 6: print('VI')
            elif number == 7: print('VII')
            elif number == 8: print('VIII')
            elif number == 9: print('IX')
            else: print('X')

            break


Roman_numerals()