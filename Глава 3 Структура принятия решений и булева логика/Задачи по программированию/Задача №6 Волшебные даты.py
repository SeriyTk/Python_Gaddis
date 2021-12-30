def Magic_dates():
    day = int(input('Введите день в числовом формате: '))
    month = int(input('Введите месяц в числовом формате: '))
    year = int(input('Введите год: '))
    if day * month == year:
        print('Дата волшебная.')
    else:
        print("Дата не волшебная.")


Magic_dates()
