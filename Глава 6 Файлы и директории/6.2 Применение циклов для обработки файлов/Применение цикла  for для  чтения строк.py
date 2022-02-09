# for переменная in файловый_объект:
        # инструкция
        # инструкция
def read_sales2():
    with open(r'G:\sales.txt') as file_sales:
        for line in file_sales:
            print(float(line))

    print('Данные из файла считаны.')

read_sales2()