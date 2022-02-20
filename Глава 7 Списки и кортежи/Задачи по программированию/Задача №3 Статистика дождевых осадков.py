def list_rainfall(par):
    rainfall = []
    for i in range(par):
        rainfall.append(float(input(f'Количество дождевых осадков за месяц №{i + 1}: ')))
    return rainfall


def get_total_year(par):
    total_rainfall = 0
    for i in par:
        total_rainfall += i
    return total_rainfall



def Rainfall_Statistics():
    year = 12
    list_r = list_rainfall(year)
    total = get_total_year(list_r)
    print(f'''
Количество дождевых осадков за год {total};
среднее ежемесячное количество дождевых осадков {(total / year):.2f};
в месяце №{(list_r.index(min(list_r))) + 1} было минимальное количество осадков {min(list_r)};
в месяце №{(list_r.index(max(list_r))) + 1} было максимальное количество осадков {max(list_r)}.
''')


Rainfall_Statistics()
