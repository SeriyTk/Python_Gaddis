def write_sales():
    num_days = int(input('Зa какое количество дней Вы располагаете продажами? '))
    with open('sales.txt', 'w') as sales_file:
        for count in range(num_days):
            sales = float(input(f'Введите продажи за день №{count + 1}: '))
            sales_file.write(f'{sales}\n')

    print('Данные записаны в sales.txt. ')

if __name__ == '__main__': write_sales()