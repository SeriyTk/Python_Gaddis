WEIGHT = 100


def Cost_of_delivery():
    package_weight = float(input('Масса пакета в граммах: '))
    if package_weight <= 200: print(f'{package_weight / WEIGHT * 150:.2f} руб.')
    elif 200 < package_weight <= 600: print(f'{package_weight / WEIGHT * 300:.2f} руб.')
    elif 600 < package_weight <= 1000: print(f'{package_weight / WEIGHT * 400:.2f} руб.')
    elif 1000 < package_weight: print(f'{package_weight / WEIGHT * 475:.2f} руб.')


Cost_of_delivery()
