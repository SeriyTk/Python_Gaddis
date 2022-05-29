def rainfall_thickness():
    years = int(input('Количество лет: '))
    total = 0
    for year in range(years):
        print(f'Год № {year + 1}')
        for month in range(12):
            rainfall_thickness = float(input(f'Толщина осадков год №{year + 1}, месяц №{month + 1}: '))
            total += rainfall_thickness

    print(f'''
Количество месяцев: {years *12};
общее количество миллиметров дождевых осадков: {total};
средняя толщина дождевых осадков: {total / (years *12):.2f}

''')


rainfall_thickness()
