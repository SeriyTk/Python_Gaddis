def condition(total):
    while True:
        purchase_amount = float(input('Величина покупки: '))
        total += purchase_amount
        if input('Хотите продолжить покупки? ') != 'y':
            break
    return total
def result(total, FEDERAL_TAX, REGIONAL_TAX):
    federal_tax = total * FEDERAL_TAX
    regional_tax = total * REGIONAL_TAX
    total_tax = federal_tax + regional_tax
    total_sum = total + total_tax
    return federal_tax, regional_tax, total_tax, total_sum
def printo(total, federal_tax, regional_tax, total_tax, total_sum):
    print(f'''Сумма покупки {total},
федеральный налог с продаж {federal_tax},
региональный налог с продаж {regional_tax},
общая сумма продажи {total_sum}.''')