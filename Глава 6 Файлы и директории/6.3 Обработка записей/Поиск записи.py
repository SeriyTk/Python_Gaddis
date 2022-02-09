def search_coffee_record():
    with open(r'G:\coffee.txt') as coffee_file:
        flag = False
        search = input('Введите искомое описание: ')
        descr = coffee_file.readline()
        while descr != '':
            qty = float(coffee_file.readline())
            descr = descr.rstrip()
            if descr == search:
                print(f'Название: {descr}.')
                print(f'Количество: {qty}.')
                print()
                flag = True
            descr = coffee_file.readline()
        if not flag:
            print('Ничего не найдено.')

search_coffee_record()

