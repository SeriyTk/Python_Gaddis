def sale_price():
    original_price = float(input('Введите исходную цену товара: '))
    sale_price = original_price - (original_price * 0.2)
    print(f'Отпускная цена составляет {sale_price}')

sale_price()
