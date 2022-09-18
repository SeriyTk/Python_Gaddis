import cashregister as cashreg

def main():
    cr = cashreg.CashRegister()
    while True:
        if input('Хотите выбрать товар? ').lower() != "д": break
        else:
            descr = input('Описание: ')
            amount = input('Количество: ')
            price = float(input('Цена: '))

            cr.purchase_item(cashreg.RetailItem(descr, amount, price))
    print('-------------------------------------------------------------')
    cr.show_items()
    print('-------------------------------------------------------------')
    print("Общая стоимость:")
    cr.get_total()

if __name__ == '__main__': main()