while True:
    a = int(input('Введите число №1: '))
    b = int(input('Введите число №2: '))
    print(f'Сумма чисел {a} и {b} равна {a + b}.')
    print('Хотите продолжить?')
    print('Введите д - если да или любое значение если нет.')
    answer = input(': ')
    if answer != 'д':
        print('Программа завершена.')
        break
