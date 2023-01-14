def Average_layer_thickness():
    total_month = 0
    total_rainfall = 0
    number_of_years = int(input("Количество лет: "))
    for year in range(number_of_years):
        print(f'Год № {year + 1}')
        for month in range(12):
            rainfall = int(input(f'Количестово осадков в месяце №{month + 1}: '))
            total_month += 1
            total_rainfall += rainfall

    print(f'''
Количество месяцев: {total_month};
общее количество миллиметров дождевых осадков: {total_rainfall}
среднюю толщину слоя дождевых осадков в месяц: {total_rainfall / total_month:.2f}
''')


Average_layer_thickness()