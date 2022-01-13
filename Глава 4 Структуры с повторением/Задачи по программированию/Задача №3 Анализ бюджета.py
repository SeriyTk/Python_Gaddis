def Budget_analysis(months_sum, amount_sum):
    total = 0.0
    for amount in range(amount_sum):
        sum = float(input(f'Сумма расходов №{amount + 1}: '))
        total += sum
    if total > months_sum:
        print(f'Перерасход {total - months_sum:.2f}.')
    else:
        print(f'Экономия {months_sum - total:.2f}.')
        
total_sum = float(input('Сумма на месяц: '))
amount = int(input('Количество трат: '))

Budget_analysis(total_sum, amount)
