def Car_expenses():
    loan_payment = get_loan_payment()
    insurance = get_insurance()
    gas = get_cost_gas()
    oil = get_cost_oil()
    tires = get_tires()
    maintenance = get_maintenance()
    sum_month = loan_payment + insurance + gas + oil + tires + maintenance
    print(f"Месячные расходы: {sum_month}.")
    print(f'Годовые расходы: {sum_month * 12}.')

def get_loan_payment():
    return float(input('Платеж по кредитам: '))
def get_insurance():
    return float(input('Страховка: '))
def get_cost_gas():
    return float(input('Бензин: '))
def get_cost_oil():
    return float(input('Масло: '))
def get_tires():
    return float(input('Шины: '))
def get_maintenance():
    return float(input('Тех.обслуживание: '))

Car_expenses()