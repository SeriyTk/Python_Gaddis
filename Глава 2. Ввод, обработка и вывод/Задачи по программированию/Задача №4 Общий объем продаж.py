SALE_TAX = 0.07


def Total_Sales():
    total_price = 0
    for numer in range(5):
        price = float(input(f'Цена товара № {numer + 1}: '))
        total_price += price

    grand_total = total_price + (total_price * SALE_TAX)
    print(f'Накопленная стоимость приобретенного товара {grand_total:,.2f}')


Total_Sales()
