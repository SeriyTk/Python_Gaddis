MARK_UP = 2.5
def retail_no_validation():
    while True:
        another = input('Ecть товар? (Введите д, если да): ')
        if another == 'д' or another == 'Д':
            wholesale = float(input("Bвeдитe оптовую стоимость товара: "))
            while wholesale < 0:
                print('ОШИБКА: стоимость не может быть отрицательной.')
                wholesale = float(input("Bвeдитe правильную оптовую стоимость товара: "))
            retail = wholesale * MARK_UP
            print(f'Розничная цена: ${retail:,.2f}')
        else: print('Программа завершена.'); break


if __name__ == '__main__': retail_no_validation = retail_no_validation()
