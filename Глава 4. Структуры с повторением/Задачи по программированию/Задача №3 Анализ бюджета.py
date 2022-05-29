def Budget_Analysis():
    sum_month = float(input('Сумма на месяц: '))
    total_sum = 0
    counter = 1
    while True:
        amount_expenses = float(input(f'Статья расходов № {counter}: '))
        counter += 1
        total_sum += amount_expenses
        if '+' != input('Хотите продолжить введите +, иначе -: ') == '-': break

    print(f'Общая сумма расходов {total_sum}')
    if total_sum > sum_month: print(f'Перерасход {total_sum - sum_month}')
    elif total_sum < sum_month: print(f'Экономия {sum_month - total_sum}')
    else: print("Уложились точно")


Budget_Analysis()
