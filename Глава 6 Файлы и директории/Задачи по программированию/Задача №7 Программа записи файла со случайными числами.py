import random as ran


def random_numbers():
    with open(r'G:\number_file.txt', 'w') as f:
        for i in range(int(input('Количество случайных чисел: '))):
            print(ran.randint(1, 500), file=f)
    print('Случайные числа в файл занесены.')
    with open(r'G:\number_file.txt') as f:
        for i in f:
            print(int(i))
random_numbers()


    

