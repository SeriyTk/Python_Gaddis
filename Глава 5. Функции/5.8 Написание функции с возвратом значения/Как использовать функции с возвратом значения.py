DISCOUNT_PERCENTAGE = 0.20


def main():
    reg_price = get_reg_price()
    sale_price = reg_price - discount(reg_price)
    print(f'Отпускная цена составляет ${sale_price:.2f}', sep=' ')

def  get_reg_price(): return float(input('Обычная цена товара: '))
def discount(price): return price * DISCOUNT_PERCENTAGE


main()
