# Сохраненные в файле данные часто организованы в виде записей. Запись  - набор данных об объекте, а поле  -  это
# отдельная порция данных в записи.
def save_records():
    with open(r'G:\квартплата.txt', 'w') as file_kvart:
        print(input('Какой месяц: '), file=file_kvart)
        for count in range(2):
            print(input('За что платим: '), file=file_kvart)
            print(input('Показания счетчика: '), file=file_kvart)
            print()
    print('Данные в файл занесены.')

def read_records():
    with open(r'G:\квартплата.txt') as file_kvart:
        month = file_kvart.readline()
        print(f'{month}')
        name = file_kvart.readline()
        while name != '':
            id = file_kvart.readline()
            print(f'Услуга: {name.rstrip()}')
            print(f'Показания: {id.rstrip()}')
            name = file_kvart.readline()


read_records()
