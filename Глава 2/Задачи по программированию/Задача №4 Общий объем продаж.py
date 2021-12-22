def Total_sales():
    SALES_TAX = 0.07
    number_units = int(input('Количество единиц товара: '))
    total_sum = 0
    for unit in range(number_units):
        price_unit = float(input(f'Цена товара № {unit+1}: '))
        total_sum += price_unit
    tax_amount = total_sum * SALES_TAX
    total_amount = total_sum + tax_amount
    print(f'''
    Стоимость приобретенного товара {total_sum},
    сумма налога с продаж {tax_amount:.2f},
    итоговая сумма {total_amount}.
''')


Total_sales()
