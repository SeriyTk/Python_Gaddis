NUM_EMPLOYEES = 6

def main():
    hours = [float(input(f'Количество отработанных часов сотрудником №{index + 1}: ')) for index in range(NUM_EMPLOYEES)]
    pay_rate = float(input('Bвeдитe почасовую ставку оплаты: '))
    numer = 0
    for hour in hours:
        numer += 1
        gross_pay = hour * pay_rate
        print(f'Зарплата сотрудника №{numer}: {gross_pay:.2f}')

main()