def write_sales():
    with open(r'G:\sales.txt', 'w') as file_sales:
        num_days = int(input('За какое количество дней Вы располагаете продажами? '))
        for day in range(1, num_days + 1):
            print(input(f'Введите продажи за день №{day}: '), file=file_sales)
    print('Данные в файл записаны.')


def read_sales():
    with open(r'G:\sales.txt') as file_sales:
        line = file_sales.readline()
        while line != '':
            print(float(line))
            line = file_sales.readline()

    print('Данные из файла считаны.')

read_sales()
