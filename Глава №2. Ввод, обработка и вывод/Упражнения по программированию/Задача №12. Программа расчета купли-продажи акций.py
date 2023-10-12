NUMBER_SHARES = 2000
COMMISSION = 0.03
PURCHASE = 40.0
SALE = 42.75
def Purchase_Sale_Shares():
    purchase_amount = NUMBER_SHARES * PURCHASE
    purchase_commission = purchase_amount * COMMISSION
    total_purchase = purchase_amount + purchase_commission
    sales_amount = NUMBER_SHARES * SALE
    sales_commission = sales_amount * COMMISSION
    total_sales = sales_amount + sales_commission
    amount_income = total_sales - total_purchase
    print(f'''
Сумма уплаченная за акции {purchase_amount:.2f};
сумма комиссии, уплаченная брокеру при покупке акций {purchase_commission:.2f};
полная сумма покупки {total_purchase};
сумма продажи акций {sales_amount:.2f};
сумма комиссии, уплаченная брокеру при продаже акций {sales_commission:.2f};
полная сумма продажи {total_sales}
сумма дохода {amount_income}
''')


if __name__ == '__main__': Purchase_Sale_Shares = Purchase_Sale_Shares()
