def main():
    total = 0
    for month in range(12):
        total_month = 0
        print(f'Месяц №{month + 1}:')
        кредит = float(input('Платеж по кредиту: '))
        страховка = float(input('Страховка: '))
        бензин = float(input('Бензин: '))
        масло = float(input('Машинное масло: '))
        шины = float(input('Шины: '))
        тех = float(input('Техобслуживание: '))
        total_month = кредит + страховка + бензин + масло + шины + тех
        print(f'Расходы в месяце №{month + 1}: {total_month}')
        total += total_month
    print(f'Общая годовая стоимость расходов {total}')



main()
