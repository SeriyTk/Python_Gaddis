def Area_calc():
    ACRE = 4046.86
    area = float(input('Общее количество квадратных метров: '))
    total_acre = area / ACRE
    print(f'{total_acre:,.7f}')

Area_calc()