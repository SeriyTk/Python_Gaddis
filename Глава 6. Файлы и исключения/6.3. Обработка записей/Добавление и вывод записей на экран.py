def add_coffee_record():
    with open('coffee.txt', 'a') as coffee_file:
        while True:
            print('Хотите создать запись?')
            another = input('Д = да, все остальное = нет: ' )
            if another == 'д' or another == 'Д':
                print('Введите следующие данные о кофе:')
                descr = input('Описание: ')
                qty = int(input('Koличecтвo (в фунтах): '))

                coffee_file.write(f'{descr}\n')
                coffee_file.write(f'{qty}\n')
            else: print('Данные добавлены в coffee.txt.'); break

    if __name__ == '__main__': add_coffee_record()

def show_coffee_record():
    with open('coffee.txt') as coffee_file:
        while True:
            descr = coffee_file.readline().rstrip()
            if descr == '': break
            else:
                qty = coffee_file.readline().rstrip()

                print(f'Описание: {descr}')
                print(f'Количество: {qty}')

if __name__ == '__main__': show_coffee_record()