def search_coffee_records():
    flag = False
    search = input('Введите искомое описание: ')
    with open('coffee.txt') as coffee_file:
        descr = coffee_file.readline()
        while descr != '':
            qty = float(coffee_file.readline())
            descr = descr.rstrip('\n')
            if descr == search:
                print(f'Oпиcaниe: {descr}')
                print(f'Количество: {qty}')
                print()
                flag = True
            descr = coffee_file.readline()

        if not flag: print('Этo значение в файле не найдено.')

if __name__ == '__main__': search_coffee_records()