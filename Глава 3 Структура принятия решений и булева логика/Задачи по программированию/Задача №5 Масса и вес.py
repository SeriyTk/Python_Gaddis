def Mass_and_weight():
    mass = float(input('Введите массу тела в килограммах: '))
    weight = get_weight(mass)
    if weight > 500:
        print('Тело слишком тяжелое.')
    elif weight < 100:
        print('Тело слишком легкое.')
    else:
        print('Вес тела нормальный.')


def get_weight(mass):
    return mass * 9.8

Mass_and_weight()
