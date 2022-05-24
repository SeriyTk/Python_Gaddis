BASE_HOURS = 40
OT_MULTIOLIER = 1.5

def auto_repair_payroll():
    hours = float(input('Количество отработанных часов: '))
    pay_rate = float(input('Почасоввая ставка оплаты труда: '))
    if hours > BASE_HOURS:
        overtime_hours = hours - BASE_HOURS
        overtime_pay = overtime_hours * pay_rate * OT_MULTIOLIER

        gross_pay = BASE_HOURS * pay_rate + overtime_pay
    else:
        gross_pay = hours * pay_rate
    print(f'Зарплата составляет {gross_pay:,.2f}', sep=' ')

auto_repair_payroll()