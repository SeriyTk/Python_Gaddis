YEAR = 12
def Car_expenses():
    total = 0
    for month in range(YEAR):
        credit_payment = float(input(f'Платеж по кредиту в месяц №{month + 1}: '))
        insurance = float(input(f'Страховка в месяц №{month + 1}: '))
        petrol = float(input(f"Бензин в месяц №{month + 1}: "))
        machine_oil = float(input(f"Машинное масло в месяц №{month + 1}: "))
        tires = float(input(f"Шины в месяц №{month + 1}: "))
        maintenance = float(input(f"Техобслуживание в месяц №{month + 1}: "))
        total_month = credit_payment + insurance + petrol + machine_oil + tires + maintenance
        total += total_month
        print()
        print(f'Общая стоимость за месяц №{month + 1}: {total_month}')
        print()
    print(f'Годовая стоимость расходов: {total}')

if __name__ == '__main__': Car_expenses()