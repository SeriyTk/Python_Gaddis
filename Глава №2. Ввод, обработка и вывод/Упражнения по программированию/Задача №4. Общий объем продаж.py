SALES_TAX = 0.07
def Total_sales():
    total = 0
    for i in range(5): price = float(input(f'Цена товара №{i + 1}: ')); total += price
    print(f'''
Накопленная стоимость приобретенных товаров {total}
сумма налога {(total * SALES_TAX):.2f}
итоговая сумма {total + (total * SALES_TAX)}
''')


if __name__ == '__main__': Total_sales = Total_sales()
