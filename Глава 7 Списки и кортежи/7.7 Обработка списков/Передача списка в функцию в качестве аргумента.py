def get_total_num(par):
    total = 0
    for i in par:
        total += i
    return total


def total_function():
    numbers = [2, 4, 6, 8, 10]
    return get_total_num(numbers)


print(f'Сумма всех чисел {total_function()}.')
