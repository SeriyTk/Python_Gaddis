def purchase_and_sale_of_shares():
    STOCK = 2000
    START_PRICE = 40.00
    END_PRICE = 40.75
    COMMISSION = 0.03
    purchase_value = STOCK * START_PRICE + (STOCK * START_PRICE) * COMMISSION
    sale_value = STOCK * END_PRICE - (STOCK * END_PRICE) * COMMISSION
    print(f'''
    За акции было уплочено {STOCK * START_PRICE},
    комиссия уплоченная брокеру {(STOCK * START_PRICE) * COMMISSION},
    акции были проданы за {STOCK * END_PRICE},
    комиссия уплоченная брокеру {(STOCK * END_PRICE) * COMMISSION}.
''')
    if sale_value - purchase_value > purchase_value:
        print(f'Вы заработали {sale_value - purchase_value}.')
    elif sale_value - purchase_value < purchase_value:
        print(f'Вы ушли в минус на {sale_value - purchase_value}')
    else:
        print('По нулям.')


purchase_and_sale_of_shares()
