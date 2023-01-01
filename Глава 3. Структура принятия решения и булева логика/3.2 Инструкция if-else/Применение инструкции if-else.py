def auto_repair_payrol():
    BASE_HOURS = 40
    ОF_MULTIPLIER = 1.5
    while True:
        hours = float(input('Bвeдитe количество отработанных часов: '))
        pay_rate = float(input('Bвeдитe почасовую ставку оплаты труда: '))
        if hours > BASE_HOURS:
            overtime_hours = hours - BASE_HOURS
            overtime_pay = overtime_hours * pay_rate * ОF_MULTIPLIER
            gross_pay = BASE_HOURS * pay_rate + overtime_pay
        else: gross_pay = hours * pay_rate
        print(f'Заработная плата до удержаний составляет: ${gross_pay:,.2f}. ')
        enter = input('Хотите продолжить? Нажмите д: ')
        if enter != 'д': print('Программа завершена.'); break



auto_repair_payrol()