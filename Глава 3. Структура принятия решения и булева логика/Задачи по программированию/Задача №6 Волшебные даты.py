def Magic_dates():
    day = int(input('Число дня: '))
    month = int(input('Ввести месяц в числовой форме: '))
    year = int(input('Двузначный год: '))
    sum_dates = month * day
    if sum_dates == year: print('Волшебная дата.')
    else: print("Дата не волшебная.")


Magic_dates()
