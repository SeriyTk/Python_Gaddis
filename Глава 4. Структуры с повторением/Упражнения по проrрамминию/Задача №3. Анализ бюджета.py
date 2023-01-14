def Budget_Analysis():
    total = 0
    count = 1
    while True:
        enter = input("Запустить программу?д - если да, пробел если нет: ")
        if enter == '': print('Программа завершена.'); break
        else:
            month_sum = float(input('Сумма выделяемая на месяц: '))
            while True:
                individual_item = float(input(f'Статья расходов №{count}: '))
                total += individual_item
                count += 1
                print('Ввести еще одну статью расходов?')
                entr = input('д - если да, пробел если нет: ')
                if entr == '': break
        break
    print()
    print(f'Сумма расходов на месяц {total:,.2f}')
    if total == month_sum: print('Вы уложились.')
    elif total > month_sum: print(f'Вы перерасходовали {(total - month_sum):,.2f}')
    elif total < month_sum: print(f'Вы сэкономили {(month_sum - total):,.2f}')



Budget_Analysis()