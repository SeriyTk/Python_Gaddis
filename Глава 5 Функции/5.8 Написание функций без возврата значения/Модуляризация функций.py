def commission_rate():
    sales = get_sales()  # Сумма продаж
    advanced_pay = get_advanced_pay()  # Аванс
    comm_rate = determine_comm_rate(sales)  # Комиссионные
    pay = sales * comm_rate - advanced_pay
    if pay > 0:
        print(f'Выплата составляет ${pay}.')
    else:
        print(f'Вы торчите {pay}.')


def get_sales():
    return float(input('Введите сумму продаж: '))


def get_advanced_pay():
    return float(input('Аванс: '))


def determine_comm_rate(sales):
    if sales < 10000:
        comm_rate = 0.1
    elif 10000 <= sales <= 14999:
        comm_rate = 0.12
    elif 15000 <= sales <= 17999:
        comm_rate = 0.14
    elif 18000 <= sales <= 21999:
        comm_rate = 0.16
    else:
        comm_rate = 0.18

    return comm_rate


commission_rate()