import cellphone as cp

def main():
    man = input('Производитель: ')
    mod = input('Модель: ')
    retail = float(input('Розничная цена: '))

    phone = cp.CellPhone(man, mod, retail)

    print('---------------------------------------------------------')
    print ('Вот введенные Вами данные:')
    print(f'Производитель: {phone.get_manufact()}')
    print(f'Модель: {phone.get_model()}')
    print(f'Розничная цена: {phone.get_price()}')

if __name__ == '__main__': main()