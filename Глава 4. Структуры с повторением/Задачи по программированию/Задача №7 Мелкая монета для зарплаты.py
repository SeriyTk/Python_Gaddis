def small_coin():
    days = int(input('Количество дней: '))
    coin = 0
    print('День\tЗ.П')
    for day in range(1, days + 1):
        if day <= 2: coin += 1; print(f'{day}  \t      {coin}')
        elif day >= 3: coin *= 2; print(f'{day}  \t      {coin}')
    print()
    print(f'Зарплата {coin / 100:,.2f}руб.')







small_coin()
