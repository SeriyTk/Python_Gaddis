def auto_repair_payroll():
    BASE_HOURS = 40
    МULTIPLIER = 1.5
    hours = float(input('Количество отработанных часов: '))
    pay_rate = float(input('Почасовая ставка: '))
    if hours > BASE_HOURS:
        salary = get_salary(hours, pay_rate)
        overtime_pay = get_overtime_pay(hours, pay_rate, BASE_HOURS, МULTIPLIER)
        print(f'Зарплата со сверхурочными составит {(salary + overtime_pay):.2f}.')
    else:
        salary = get_salary(hours, pay_rate)
        print(f'Зарплата составит {salary:.2f}.')


def get_salary(hours, pay_rate):
    salary = hours * pay_rate
    return salary


def get_overtime_pay(hours, pay_rate, BASE_HOURS, МULTIPLIER):
    overtime_hours = hours - BASE_HOURS
    overtime_pay = overtime_hours * pay_rate * МULTIPLIER
    return overtime_pay


auto_repair_payroll()
