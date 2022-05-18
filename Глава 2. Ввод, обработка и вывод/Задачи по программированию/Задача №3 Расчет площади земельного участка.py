AKR = 4047


def Area_calculation():
    area = float(input('Площадь земельного участка в кв.м: '))
    acre_land = area / AKR
    print(f'Будет {acre_land:.2f} акров земли')


Area_calculation()
