def get_values():
    values = []
    while True:
        values.append(int(input('Введите число: ')))
        print('Желаете добавить еще одно число?')
        if input('д =да, все остальное= нет: ') != 'д':
            print("Данные в список занесены.")
            break
    return values


def return_list():
    return get_values()


print(f'Числа в списке {return_list()}.')
