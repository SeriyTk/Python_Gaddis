def Population():
    days = int(input('Количество дней: '))
    start = int(input('Стартовое количество: '))
    INCREASE = 0.3
    print('День\tПопуляция')
    for i in range(days):
        print(f'{i + 1}   \t\t\t  {start}')
        start += (start * INCREASE)


Population()