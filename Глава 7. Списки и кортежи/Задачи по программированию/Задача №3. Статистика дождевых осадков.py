YEAR = 12


def main():
    total = 0
    list_months = [int(input(f'Осадки за месяц №{month + 1}: ')) for month in range(YEAR)]
    for i in list_months: total += i
    average_amount = total / len(list_months)
    for i in list_months:
        if i == min(list_months): print(i)
    print(f'''
Количество дождевых осадков за год: {total};
среднее ежемесячное количество дождевых осадков: {average_amount};

    ''')


main()
