class CellPhone:
    # Метод __init__ инициализирует атрибуты.
    def __init__(self, manufact, model, price):
        self.__manufact = manufact
        self.__model = model
        self.__retail_price = price

    # Метод set_manufact принимает аргумент для производителя телефона.

    def set_manufact(self, manufact):
        self.__manufact = manufact

    # Метод set_model принимает аргумент для номера модели телефона.

    def set_model(self, model):
        self.__model = model

    # Метод set_retail_price принимает аргумент для розничной цены телефона.

    def set_retail_price(self, price):
        self.__retail_price = price

    # Метод get_manufact возвращает производителя телефона.
    def get_manufact(self):
        return self.__manufact

    # Метод get_model возвращает номер модели телефона.
    def get_model(self):
        return self.__model

    # Метод get retail_price возвращает розничную цену телефона.
    def get_retail_price(self):
        return self.__retail_price



# Функция make_list получает от пользователя данные
# о пяти телефонах, а затем возвращает список
# объектов CellPhoпe, содержащих эти данные.
def make_list():
    # Создать пустой список.
    phone_list = []

    # Добавить пять объектов CellPhone в список.
    num_phones = int(input('Количество телефонов: '))
    start = num_phones - (num_phones - 1)
    end = num_phones + 1
    for count in range(start,end):
        print(f'Телефон № {count}:')
        # Создать новый объект CellPhone в памяти
        # и присвоить его переменной phone.
        phone = CellPhone(input('Производитель: '), input('Модель: '), input('Розничная цена: '))

        # Добавить объект в список.
        phone_list.append(phone)

    # Вернуть список.
    return phone_list

# Функция display_list принимает список с объектами
# CellPhone в качестве аргумента и показывает
# хранящиеся в каждом объекте данные.

def display_list(phone_list):
    for item in phone_list:
        print(item.get_manufact())
        print(item.get_model())
        print(item.get_retail_price())
        print()

# Функция показывает данные
def display_data(par):
    print(f'Производитель: {par.get_manufact()}')
    print(f'Модель: {par.get_model()}')
    print(f'Розничная цена: {float(par.get_retail_price()):.2f}', sep=' ')
    print()