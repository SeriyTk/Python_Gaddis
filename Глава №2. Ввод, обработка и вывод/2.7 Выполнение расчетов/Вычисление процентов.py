def main():
    original_price = float( input ("Bвeдитe исходную цену товара: "))
    discount = original_price * 0.2
    sale_price = original_price - discount
    print('Отпускная цена составляет', sale_price)

if __name__ == '__main__': main()
