def Magic_dates():
    day = int(input('День: '))
    month = int(input('Месяц: '))
    year = int(input('Год: '))
    month_day = month * day
    if month_day == year: print(f'Дата {day}.{month}.{year} магическая.')
    else: print(f'Дата {day}.{month}.{year} не магическая.')

Magic_dates()