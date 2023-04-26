def room_numbers():
    room_numbers = {}
    while True:
        enter = input('Вводите значения? д/н: ')
        if enter.lower() == 'д':
            num_kurs = input('Номер курса: ')
            room_numbers[num_kurs] = input("Номер аудитории: ")
        elif enter.lower() == 'н': break
    print('Номер курса\tНомер аудитории')
    for k, v in room_numbers.items(): print(f'{k}   \t\t    {v}')
