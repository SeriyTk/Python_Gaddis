def Budget_analysis():
    amount_month = float(input('Сумма выделенная на месяц: '))
    total = 0.0
    while True:
        question = input('Ввести статью расходов? Если "да" - то д: ')
        if question == 'д' or question =='Д':
            amounts_items = float(input('Сумма отдельной части расходов: '))
            total += amounts_items
        else: print('Программа завершена.'); break
    print()
    print(f"Выделено {amount_month:.2f}")
    print(f'Израсходован {total:.2f}')
    if amount_month > total: print(f'Сэкономлено {amount_month - total}')
    elif amount_month < total: print(f'Перерасход {total - amount_month}')
    else: print("При своих.")



if __name__ == '__main__': Budget_analysis = Budget_analysis()
