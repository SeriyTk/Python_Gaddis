# Функция с возвратом значения имеет инструкцию return, которая возвращает значение
# в ту часть программы, которая ее вызвала.
# def имя_функции():
# инструкция
# инструкция
# return выражение

def total_ages():
    first_age = int(input('Введите свой возвраст: '))
    second_age = int(input('Введите возвраст своей жены: '))
    print(f'Общее количество лет {total_age(first_age, second_age)}.')


def total_age(first_age, second_age):
    return first_age + second_age


print('----------------------------------')
DISCOUNT_PERCENTAGE = 0.2


def sale_prlce():
    price = get_regular_price()
    sale_prlce = price - discount(price)
    print(f'Отпускная цена товара составляет ${sale_prlce:.2f}', sep=' ')


def get_regular_price():
    return float(input('Введите обычную цену товара: '))


def discount(price):
    return price * DISCOUNT_PERCENTAGE


sale_prlce()
