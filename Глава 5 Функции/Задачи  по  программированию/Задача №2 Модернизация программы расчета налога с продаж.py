FEDERAL_TAX = 0.05
REGIONAL_TAX = 0.025


def sales_tax_calculation_program(purchase_amount):
    print(f'''
        Сумма покупки равна {purchase_amount},
        федеральный налог с продажи равен {purchase_amount * FEDERAL_TAX},
        региональный налог с продажи равен {purchase_amount * REGIONAL_TAX},
        общий налог с продаж равен {(purchase_amount * FEDERAL_TAX) + (purchase_amount * REGIONAL_TAX)},
        общая сумма продажи будет {purchase_amount + ((purchase_amount * FEDERAL_TAX) + (purchase_amount * REGIONAL_TAX))}. 
    ''')


purchase_amount = float(input('Введите величину покупки: '))
sales_tax_calculation_program(purchase_amount)
