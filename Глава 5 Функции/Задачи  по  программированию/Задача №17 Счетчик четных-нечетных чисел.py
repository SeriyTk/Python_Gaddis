import random as r


def Even_odd_number_counter():
    total_even = 0
    total_odd = 0
    for i in range(100):
        num = r.randint(1, 100)
        if num % 2 == 0:
            print(f'Число {num} четное.')
            total_even += 1
        else:
            print(f'Число {num} не четное.')
            total_odd += 1

    print(f'Количетство четных чисел: {total_even}, количество нечетных чисел: {total_odd}.')


Even_odd_number_counter()
