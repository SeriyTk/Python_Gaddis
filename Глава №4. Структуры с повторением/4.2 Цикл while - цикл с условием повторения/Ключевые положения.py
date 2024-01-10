def commission():
    keep_going = 'д'
    while keep_going == 'д':
        sales = float(input('Bвeдитe объем продаж: '))
        comm_rate = float(input('Bвeдитe ставку комиссионных: '))
        commission = sales * comm_rate
        print(f'Комиссионное вознаграждение составляет ${commission:,.2f}.')
        keep_going = input('Хотите продолжить? Введите д, если да: ')

    print("Программа завершена.")


if __name__ == '__main__': commission = commission()
