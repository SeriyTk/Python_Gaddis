my_list = [10, 20, 30, 40]
print(my_list)
my_list[1] = 50
print(my_list)

NUM_DAYS = 5


def sales_list():
    sales = [0] * NUM_DAYS
    index = 0
    while index < NUM_DAYS:
        sales[index] = float(input(f'День № {index + 1}: '))
        index += 1
    print('Значения которые были введены.')
    for i in sales:
        print(i)


sales_list()
