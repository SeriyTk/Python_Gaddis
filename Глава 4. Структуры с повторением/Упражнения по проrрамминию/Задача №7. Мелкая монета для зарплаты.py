def small_coin():
    COIN = 1
    total_coins = 0
    total_sum = 0
    num_days = int(input('Количество дней: '))
    print('Дни\tДеньги')
    for day in range(num_days + 1):
        if 1 <= day <= 2: total_coins += COIN; print(f'{day}\t\t {total_coins}')
        elif day >= 3: total_coins *= 2; print(f'{day}\t\t {total_coins}')
        total_sum += total_coins

    print(f'''Общая сумма {total_sum /100:,.2f}''')

small_coin()