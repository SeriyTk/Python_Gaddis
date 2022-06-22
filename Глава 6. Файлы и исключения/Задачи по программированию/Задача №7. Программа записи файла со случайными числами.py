import random


def main():
    with open('rand_num.txt', 'w') as out_file:
        for i in range(int(input('Количество случайных чисел: '))):
            print(random.randint(1, 500), file=out_file)


main()
