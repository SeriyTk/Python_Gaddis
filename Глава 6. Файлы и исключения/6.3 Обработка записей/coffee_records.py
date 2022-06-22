import os

def add_coffee_record():
    with open('coffee.txt', 'a') as coffee_file:
        while True:
            if input('Введите данные о кофе? Если нет - "нет": ') == 'нет': break
            else:
                print(input('Описание: '), file=coffee_file)
                print(input('Количество в фунтах: '), file=coffee_file)
        print('Данные добавлены в coffee. txt. ')

def show_coffee_records():
    with open('coffee.txt') as coffee_file:
        while True:
            descr = coffee_file.readline().rstrip()
            if not descr: break
            else:
                qty = float(coffee_file.readline().rstrip())

                print('Описание:', descr)
                print('Количество:', qty)
                print()

def search_coffee_records():
    search = input('Что ищите? ')
    with open('coffee.txt') as coffee_file:
        while True:
            descr = coffee_file.readline().rstrip()
            if not descr: break
            else:
                qty = float(coffee_file.readline().rstrip())
                if descr == search:
                    print('Описание:', descr)
                    print('Количество:', qty)
                    print()
        else: print('Этo значение в файле не найдено.')

def search_coffee_records1():
    flag = False
    search = input('Что ищите? ')
    with open('coffee.txt') as coffee_file:
        while True:
            descr = coffee_file.readline().rstrip()
            if not descr: break
            else:
                qty = float(coffee_file.readline().rstrip())
                if descr == search:
                    print('Описание:', descr)
                    print('Количество:', qty)
                    print()
                    flag = True
        if not flag: print('Этo значение в файле не найдено.')

def modify_coffee_records():
    flag = False
    search = input('Что ищите? ')
    with open('coffee.txt') as coffee_file, open('temp.txt', 'w') as temp_file:
        while True:
            descr = coffee_file.readline().rstrip()
            if not descr: break
            else:
                qty = float(coffee_file.readline().rstrip())
                if descr == search:
                    new_qty = input('Новое количество: ')
                    print(descr, file=temp_file); print(new_qty, file=temp_file); flag = True
                else: print(descr, file=temp_file); print(qty, file=temp_file)

    os.remove('coffee.txt')
    os.rename('temp.txt', 'coffee.txt')

    if flag: print ('Файл обновлен.')
    else: print('Этo значение в файле не найдено.')

def delete_coffee_record():
    flag = False
    search = input('Kaкoй бренд желаете удалить? ')
    with open('coffee.txt') as coffee_file, open('temp.txt', 'w') as temp_file:
        while True:
            descr = coffee_file.readline().rstrip()
            if not descr:
                break
            else:
                qty = float(coffee_file.readline().rstrip())
                if descr != search:
                    print(descr, file=temp_file); print(qty, file=temp_file)
                else: flag = True

    os.remove('coffee.txt')
    os.rename('temp.txt', 'coffee.txt')

    if flag:
        print('Файл обновлен.')
    else:
        print('Этo значение в файле не найдено.')





