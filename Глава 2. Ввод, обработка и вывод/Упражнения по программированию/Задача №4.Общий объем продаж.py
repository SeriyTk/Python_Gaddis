def Total_Sales():
    TAX = 0.07
    total_sum = 0
    quantity_goods = int(input('Какое количество товара хотите приобрести? '))
    for i in range(quantity_goods):
        price_product = float(input(f'Стоимость товара №{i + 1}: '))
        total_sum += price_product
    total_tax = total_sum * TAX
    result = total_sum + total_tax
    print(f'''
Накопленая стоимость товаров: {total_sum:.2f};
сумма налога: {total_tax:.2f};
итоговая сумма: {result:,.2f}.
''')

Total_Sales()