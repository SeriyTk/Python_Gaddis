def Cost_delivery():
    package_weight = int(input('Введите массу пакета: '))
    if package_weight <= 200: print(f'{package_weight  / 100 * 150:,.2f}')
    elif 200 < package_weight <= 600: print(f'{package_weight  / 100 * 300:,.2f}')
    elif 600 < package_weight <= 1000: print(f'{package_weight / 100 * 400:,.2f}')
    elif package_weight > 1000: print(f'{package_weight / 100 * 475:,.2f}')


if __name__ == '__main__': Cost_delivery = Cost_delivery()
