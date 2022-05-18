SALE_TAX = 0.07
TIPS = 0.18


def food_cost():
    cost = float(input('Стоимость еды: '))

    sale_tax = cost * SALE_TAX
    tips = cost * TIPS
    total_sum = cost + sale_tax + tips

    print(f'''
Стоимость еды {cost},
чаевые {tips:.2f},
налог с продаж {sale_tax:.2f},
итоговая сумма {total_sum:.2f}.
''')


food_cost()
