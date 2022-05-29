def property_tax():
    TAX_FACTOR = 0.0065

    while True:
        print('Введите номер имущественного лота либо 0, чтобы завершить работу.')
        lot = int(input('Номер лота: '))
        if lot == 0: break
        else:
            value = float(input('Bвeдитe стоимость имущества: '))
            tax = value * TAX_FACTOR
            print(f'Налог на имущество: ${tax: .2f}', sep=' ')

    print('Программа завершена.')



property_tax()
