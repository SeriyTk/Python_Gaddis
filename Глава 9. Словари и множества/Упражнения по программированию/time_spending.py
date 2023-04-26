def time_spending():
    time_spending = {}
    while True:
        enter = input('Вводите значения? д/н: ')
        if enter.lower() == 'д':
            num_kurs = input('Номер курса: ')
            time_spending[num_kurs] = input("Время: ")
        elif enter.lower() == 'н': break
    print('Номер курса\tВремя')
    for k, v in time_spending.items(): print(f'{k}   \t\t    {v}:00')
