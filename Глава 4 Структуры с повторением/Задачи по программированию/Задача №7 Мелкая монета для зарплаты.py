def Small_coin_for_salary(days):
    penny = 0.01
    total = 0.01
    print('День\tЗарплата')
    print('-------------------')
    print(1, penny, sep='   \t \t ')
    if days > 1:
        for day in range(2, days + 1):
            penny *= 2
            print(f'{day}  \t \t {penny}')
            total += penny
    print('-------------------')
    print(f'Всего {total:.2f} руб.')


num_days = int(input('Количество дней: '))
Small_coin_for_salary(num_days)
