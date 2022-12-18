def purchase_sale_shares():
    NUMBER_SHARES = 2000
    PURCHASE_PRICE = 40
    COMMISSION = 0.03
    SELLING_PRICE = 42.75
    purchase_amount = NUMBER_SHARES * PURCHASE_PRICE
    commission_amount = purchase_amount * COMMISSION
    sale_amount = NUMBER_SHARES * SELLING_PRICE
    sales_commission = sale_amount * COMMISSION
    balance_amount = (sale_amount - sales_commission) - (purchase_amount + commission_amount)
    print(F'''
Сумма денег, уплаченная за акции  -  {purchase_amount:,.2f};
сумма комиссии, уплаченная брокеру при покупке акций - {commission_amount:,.2f};
сумма продажи - {sale_amount:,.2f};
сумма комиссии, уплаченная брокеру при продаже акций - {sales_commission:,.2f}
''')
    if balance_amount == 0: print('По нулям.')
    elif balance_amount > 0: print(f'Прибыль составила - {balance_amount:,.2f}')
    else: print(f'Убыто составил - {balance_amount:,.2f}')


purchase_sale_shares()