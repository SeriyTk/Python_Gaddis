FEDERAL_TAX = 0.05
REGIONAL_TAX = 0.025


def Sales_tax():
    total = 0
    while True:
        purchase_amount = float(input('Величина покупки: '))
        total += purchase_amount
        if input('Хотите продолжить покупки? ') != 'y':
            break

    federal_tax = total * FEDERAL_TAX
    regional_tax = total * REGIONAL_TAX
    total_tax = federal_tax + regional_tax
    total_sum = total + total_tax

    print(f'''Сумма покупки {total},
федеральный налог с продаж {federal_tax},
региональный налог с продаж {regional_tax},
общая сумма продажи {total_sum}.''')



Sales_tax()
