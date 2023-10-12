FED_TAX = 0.05
REG_TAX = 0.025
def Sales_tax():
    purchase_amount = float(input('Ввести величину покупки: '))
    fed_tax = purchase_amount * FED_TAX
    reg_tax = purchase_amount * REG_TAX
    general_sales_tax = fed_tax + reg_tax
    total_sales_amount = purchase_amount + general_sales_tax
    print(f'''
Сумма покупки {purchase_amount};
федеральный налог с продаж {fed_tax};
 региональный налог с продаж {reg_tax};
 общий налог с продаж {general_sales_tax};
 общая сумма продажи {total_sales_amount}.
''')

if __name__ == '__main__': Sales_tax = Sales_tax()
