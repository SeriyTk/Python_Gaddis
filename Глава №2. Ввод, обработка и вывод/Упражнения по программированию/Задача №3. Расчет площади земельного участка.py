ACRE = 4047
def Area_calculation():
    plot_of_land = float(input('Общее количество квадратных метров участка земли: '))
    number_of_acres = plot_of_land / ACRE
    print(f'Количество акров в этом участке {number_of_acres:.2f}')


if __name__ == '__main__': Area_calculation = Area_calculation()
