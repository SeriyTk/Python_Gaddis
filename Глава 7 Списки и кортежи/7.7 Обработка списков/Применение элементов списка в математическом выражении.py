def barista_pay():
    hours = []
    num_employees = 0
    while True:
        hours.append(float(input(f'Количество часов отработанных сотрудником № {num_employees + 1}: ')))
        num_employees += 1
        print('Еще один сотрудник?')
        if input('Если да - введите д: ') != 'д':
            print('Данные в список занесены.')
            break
    pay_rate = float(input('Bвeдитe почасовую ставку оплаты: '))
    for index in range(len(hours)):
        gross_pay = hours[index] * pay_rate
        print(f'Зарплата сотрудника № {index + 1} равна {gross_pay:.2f}.')


barista_pay()

