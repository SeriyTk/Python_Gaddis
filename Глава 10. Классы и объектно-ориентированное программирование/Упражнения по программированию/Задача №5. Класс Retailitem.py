class Retailitem:
    def __init__(self, descr, amount, price):
        self.__descr = descr
        self.__amount = amount
        self.__price = price

    def set_descr(self, descr): self.__descr = descr
    def set_amount(self, amount): self.__amount = amount
    def set_price(self, price): self.__price = price

    def get_descr(self): return self.__descr
    def get_amount(self): return self.__amount
    def get_price(self): return self.__price

    def __str__(self): return f'''
 Описание             Количество на складе                 Цена
{self.__descr} \t\t     {self.__amount}       \t\t        {self.__price}  
'''

def main():
    goods = make_list()
    display_list(goods)
def make_list():
    goods_list = []
    for i in range(2):
        descr = input('Введите описание товара: ')
        amount = input("Количество на складе: ")
        price = input('Цена: ')
        print()
        goods = Retailitem(descr, amount, price)
        goods_list.append(goods)
    return goods_list
def display_list(goods_list):
    num = 1
    for j in goods_list: print(f'Товар №{num}', end=' '); print(j); num += 1

if __name__ == '__main__': main()
