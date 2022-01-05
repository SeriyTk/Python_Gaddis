def Software_implementation():
    RETAIL = 99
    number_of_sales = int(input('Количество проданых пакетов: '))
    discount_amount, sum_sales = get_sum(RETAIL, number_of_sales)
    print(f'Сумма скидки составит {discount_amount}.')
    print(f'Общая сумма покупки {sum_sales}.')


def get_sum(RETAIL, number_of_sales):
    if 1 <= number_of_sales < 10:
        sum_sales = RETAIL * number_of_sales
    elif 10 <= number_of_sales <= 19:
        discount_amount = (RETAIL * number_of_sales) * 0.10
        sum_sales = (RETAIL * number_of_sales) - discount_amount
    elif 20 <= number_of_sales <= 49:
        discount_amount = (RETAIL * number_of_sales) * 0.20
        sum_sales = (RETAIL * number_of_sales) - discount_amount
    elif 50 <= number_of_sales <= 99:
        discount_amount = (RETAIL * number_of_sales) * 0.30
        sum_sales = (RETAIL * number_of_sales) - discount_amount
    elif number_of_sales >= 49:
        discount_amount = (RETAIL * number_of_sales) * 0.40
        sum_sales = (RETAIL * number_of_sales) - discount_amount

    return discount_amount, sum_sales


Software_implementation()
