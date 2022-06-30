import random


def main():
    num_list = [random.randint(0, 9) for i in range(7)]
    for i in num_list: print(i, end=' ')


main()
