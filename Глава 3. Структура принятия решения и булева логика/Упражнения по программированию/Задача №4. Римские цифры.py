def Roman_numerals():
    while True:
        num = int(input('Введите число от 1 до 10: '))
        if num <1 or num > 10: print('Число некорректное.')
        else:
            if num == 1: print('I'); break
            elif num == 2: print('II'); break
            elif num == 3: print('III'); break
            elif num == 4: print('IV'); break
            elif num == 5: print('V'); break
            elif num == 6: print('VI'); break
            elif num == 7: print('VII'); break
            elif num == 8: print('VIII'); break
            elif num == 9: print('IX'); break
            else: print('X'); break

Roman_numerals()