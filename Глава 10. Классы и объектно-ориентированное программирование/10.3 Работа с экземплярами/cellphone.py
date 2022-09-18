import pickle

class  CellPhone:
    def __init__(self, manufact, model, price):
        self.__manufact = manufact
        self.__model = model
        self.__price = price

    def set_manufact(self, manufact): self.__manufact = manufact
    def set_model(self, model): self.__model = model
    def set_price(self, price): self.__price = price

    def get_manufact(self): return self.__manufact
    def get_model(self): return self.__model
    def get_price(self): return self.__price
'-------------------------------------------------------------------------------------------'
def make_list():
    phones_list = []

    print('Введите данные о телефонах. ')
    for count in range(int(input("Количество телефонов: "))):
        print(f'Телефон №{count + 1}:')
        man = input('Производитель: ')
        mod = input('Модель: ')
        price = float(input('Розничная цена: '))
        print()

        phone = CellPhone(man, mod, price)

        phones_list.append(phone)

    return phones_list
'--------------------------------------------------------------------------------------------'
def display_list(phone_list):
    for item in phone_list:
        print(item.get_manufact())
        print(item.get_model())
        print(item.get_price())
        print()
'-------------------------------------------------------------------------------------------'
def dump_file(file):
    with open(file, 'wb') as out_file:
        while True:
            if input('Введете элемент данных?(д/н): ').lower() == 'н':
                print(f'Дaнныe записаны в {file}')
                break
            else:
                man = input('Производитель: ')
                mod = input("Модель: ")
                price = float(input("Розничная цена: "))
                phone = CellPhone(man, mod, price)
                pickle.dump(phone, out_file)

def load_file(file):
    with open(file, 'rb') as in_file:
        end_file = False
        while not end_file:
            try:
                phone = pickle.load(in_file)
                display_data(phone)
            except EOFError: end_file = True

def display_data(phone):
    print(f'Производитель: {phone.get_manufact()}')
    print(f'Hoмep модели: {phone.get_model()}')
    print(f'Розничная цена: ${phone.get_price():,.2f} ')
    print()

