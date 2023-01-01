def Software_Implementation():
    PRICE = 99
    number_of_packages = int(input('Количество приобретенных пакетов: '))
    if 10 <= number_of_packages < 20:
        sum = number_of_packages * PRICE
        discount = sum * 0.10
        res = sum - discount
        print(f'Скидка составит {discount}, общая сумма покупки {res}.')
    elif 20 <= number_of_packages < 50:
        sum = number_of_packages * PRICE
        discount = sum * 0.20
        res = sum - discount
        print(f'Скидка составит {discount}, общая сумма покупки {res}.')
    elif 50 <= number_of_packages < 100:
        sum = number_of_packages * PRICE
        discount = sum * 0.30
        res = sum - discount
        print(f'Скидка составит {discount}, общая сумма покупки {res}.')
    elif 100 <= number_of_packages:
        sum = number_of_packages * PRICE
        discount = sum * 0.40
        res = sum - discount
        print(f'Скидка составит {discount}, общая сумма покупки {res}.')
    else:
        sum = number_of_packages * PRICE
        print(f'Общая сумма покупки {sum}.')

Software_Implementation()