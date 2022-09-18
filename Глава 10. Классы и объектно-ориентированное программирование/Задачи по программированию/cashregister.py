class RetailItem:
    def __init__(self, descr, amount, price):
        self.__descr = descr
        self.__amount = amount
        self.__price = price

    def set_descr(self, descr): self.__descr
    def set_amount(self, amount): self.__amount
    def set_price(self, price): self.__price

    def get_descr(self): return self.__descr
    def get_amount(self): return self.__amount
    def get_price(self): return self.__price

class CashRegister:
    def __init__(self): self.__items = []

    def purchase_item(self, retail_item): self.__items.append(retail_item)

    def get_total(self):
        total = 0.0
        for item in self.__items: total +=item.get_price()
        print(f'{float(total):.2f}')

    def show_items(self):
        print("Список выбранных товаров:")
        for item in self.__items:
            print(f'Наименование: {item.get_descr()}'); print(f'Количество: {item.get_amount()}')


    def clear(self): self.__items = []
