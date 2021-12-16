def sale_pгice():
    original_price = get_original_price()
    discount = get_discount(original_price)
    sale_price = get_sale_price(original_price,discount)
    print(f'Отпускная цена товара будет {sale_price} руб.')

def get_original_price():
    original_price = float(input('Первоночальная цена товара: '))
    return original_price

def get_discount(original_price):
    discount = original_price * 0.2
    return discount

def get_sale_price(original_price,discount):
    sale_price = original_price - discount
    return sale_price

sale_pгice()

