def add_coffee_record():
    with open(r'G:\coffee.txt', 'w') as coffee_file:
        while True:
            print('Введите следующие данные о кофе.')
            print(input('Название кофе: '), file=coffee_file)
            print(input('Количество(в фунтах): '), file=coffee_file)
            print('Желаете ли Вы добавить еще одну запись?')
            if input(': ') != 'д':
                print('Программа завершена.')
                break
def show_coffee_records():
    with open(r'G:\coffee.txt') as coffee_file:
        descr = coffee_file.readline()
        while descr != '':
            qty = float(coffee_file.readline())
            print(f'Название: {descr.rstrip()}.')
            print(f'Количество: {qty}.')
            descr = coffee_file.readline()

show_coffee_records()
