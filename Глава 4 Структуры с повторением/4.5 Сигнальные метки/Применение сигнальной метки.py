def ргорегtу_tах():
    TAX = 0.0065
    while True:
        lot = int(input('Введтие номер лота, либо 0, чтобы завершить работу: '))
        if lot == 0:
            print('Программа завершена.')
            break
        else:
            value = float(input('Введите стоимость имущества: '))
            tax = value * TAX
            print(f'Налог на имущество составляет {tax:.2f}.')
ргорегtу_tах()
