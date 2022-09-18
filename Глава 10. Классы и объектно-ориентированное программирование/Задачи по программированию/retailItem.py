class RetailItem:
    def __init__(self, num , descr, amount, price):
        self.__num = num
        self.__descr = descr
        self.__amount = amount
        self.__price = price

    def set_num(self, num): self.__num
    def set_descr(self, descr): self.__descr
    def set_amount(self, amount): self.__amount
    def set_price(self, price): self.__price

    def get_num(self): return self.__num
    def get_descr(self): return self.__descr
    def get_amount(self): return self.__amount
    def get_price(self): return self.__price

def ret_list():
    retailitem_list = []
    num = 1
    while True:
        if input('Ввести данные? ').lower() != "д": break
        else:
            descr = input('Описание: ')
            amount = input('Количество на складе: ')
            price = float(input('Цена: '))
            retailitem_list.append(RetailItem(num, descr, amount, price))
            num += 1
    return retailitem_list

def display_list(retailitem_list):
    for item in retailitem_list:
        print(f'''
Товар №{item.get_num()}  \t\t {item.get_descr()} \t\t {item.get_amount()} \t\t {item.get_price()}
''')
