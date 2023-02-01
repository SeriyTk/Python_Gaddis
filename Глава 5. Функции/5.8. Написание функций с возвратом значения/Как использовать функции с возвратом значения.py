DISCOUNT_PERCENTAGE = 0.20
def sale_price():
    reg_price = get_regular_price()
    sale_price = reg_price - discount(reg_price)
    print(f'Отпускная цена составляет ${sale_price:,.2f}.')

def get_regular_price(): return float(input("Bвeдитe обычную цену товара: "))
def discount(price): return price * DISCOUNT_PERCENTAGE

if __name__ == '__main__': sale_price()