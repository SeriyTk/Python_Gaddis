MONTHS = 2
def Average_thickness():
    total_prec = 0.0
    total_months = 0
    years = int(input('Количество лет: '))
    for year in range(years):
        print(f'Год №{year + 1}.')
        for month in range(MONTHS):
            precipitation = float(input(f'Количество осадков в месяце №{month + 1}: '))
            total_prec += precipitation
            total_months += month
    print()
    print(f'''
Количество месяцев {MONTHS};
общее количество миллиметров дождевых осадков {total_prec};
средняя толщина слоя дождевых осадков в месяц {total_prec / total_months}
''')


if __name__ == '__main__': Average_thickness = Average_thickness()
