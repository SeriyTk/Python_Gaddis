import os


def delete_coffee_records():
    flag = False
    with open(r'G:\coffee.txt') as coffee_file, open(r'G:\temp.txt', 'w') as temp_file:
        search = input('Какую позицию хотите удалить? ')
        descr = coffee_file.readline()
        while descr != '':
            qty = coffee_file.readline()
            descr = descr.rstrip()
            qty = qty.rstrip()
            if descr != search:
                print(descr, file=temp_file)
                print(qty, file=temp_file)
            else:
                flag = True
            descr = coffee_file.readline()
            
    os.remove(r'G:\coffee.txt')
    os.rename(r'G:\temp.txt', r'G:\coffee.txt')
    if flag:
        print('Значение найдено и удалено.')
    else:
        print('Такого кофе нету.')


delete_coffee_records()


