BASE_HOURS = 40
ОТ_MULTIPLIER = 1.5
def auto_repair_payroll():
    hours = float(input('Bвeдитe количество отработанных часов: '))
    pay_rate = float(input('Bвeдитe почасовую ставку оплаты труда: '))

    if hours > BASE_HOURS:
        overtime_hours = hours - BASE_HOURS
        overtime_pay = overtime_hours * pay_rate * ОТ_MULTIPLIER
        gross_pay = BASE_HOURS * pay_rate + overtime_pay
    else: gross_pay = hours * pay_rate

    print(f'Заработная плата до удержаний составляет: ${gross_pay:,.2f}.')


if __name__ == '__main__': auto_repair_payroll = auto_repair_payroll()
