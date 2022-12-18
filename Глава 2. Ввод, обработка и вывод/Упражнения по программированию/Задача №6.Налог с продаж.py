def Sales_Tax():
    FED = 0.05
    REG = 0.025
    purchase_amount = float(input('Сумма покупки: '))
    reg_tax = purchase_amount * REG
    fed_tax = purchase_amount * FED
    total_tax = reg_tax + fed_tax
    total_sum = purchase_amount + total_tax
    print(f'''
Сумма покупки {purchase_amount:,.2f};
федеральный налог {fed_tax:,.2f};
региональный налог {reg_tax:,.2f};
общий налог {total_tax:,.2f};
общая сумма продажи {total_sum:,.2f}.
''')


Sales_Tax()