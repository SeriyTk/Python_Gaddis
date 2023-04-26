def names_teach():
    names_teach = {}
    while True:
        enter = input('Вводите значения? д/н: ')
        if enter.lower() == 'д':
            num_kurs = input('Номер курса: ')
            names_teach[num_kurs] = input("Преподаватель: ")
        elif enter.lower() == 'н': break
    print('Номер курса\tПреподаватель')
    for k, v in names_teach.items(): print(f'{k}   \t\t    {v}')
