def Average_rainfall_thickness(years):
    total = 0
    months = 0
    for year in range(years):
        print(f'Год №{year + 1}.')
        for month in range(12):
            precipitation_month = float(input(f'Толщина дождевых осадков за месяц №{month + 1}: '))
            total += precipitation_month
            months += 1
    print(f'Количество месяцев - {months}')
    print(f'Количество дождевых осадков - {total:,.2f}.')
    print(f'Среднее количество дождевых осадков в месяц - {total / months:.2f}.')


number_of_years = int(input('Количество лет:'))
Average_rainfall_thickness(number_of_years)
