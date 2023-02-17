import os
def modify_coffee_records():
    flag = False
    search = input('Введите искомое описание: ')
    new_qty = int(input('Bвeдитe новое количество: '))
    with open('coffee.txt') as coffee_file, open('temp.txt', 'w') as temp_file:
        descr = coffee_file.readline()
        while descr != '':
            qty = float(coffee_file.readline())
            descr = descr.rstrip('\n')
            if descr == search:
                temp_file.write(f'{descr}\n')
                temp_file.write(f'{new_qty}\n')
                flag = True
            else:
                temp_file.write(f'{descr}\n')
                temp_file.write(f'{qty}\n')
            descr = coffee_file.readline()

    os.remove('coffee.txt')
    os.rename('temp.txt', 'coffee.txt')

    if flag: print('Файл обновлен.')
    else: print('Этo значение в файле не найдено.')

if __name__ == '__main__': modify_coffee_records()