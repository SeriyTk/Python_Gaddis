class Patient:
    def __init__(self, name, adres, phone, second_contact):
        self.__name = name
        self.__adres = adres
        self.__phone = phone
        self.__sec_cont = second_contact

    def get_name(self):
        return self.__name
    def get_adres(self):
        return self.__adres
    def get_phone(self):
        return self.__phone
    def get_sec_cont(self):
        return self.__sec_cont

    def __str__(self):
        return (f'''
Информация о клиенте.
Ф.И.О.: {self.__name}
Адрес: {self.__adres}
Телефон: {self.__phone}
Контактное лицо: {self.__sec_cont}
''')

class Procedure:
    def __init__(self, proced, date, name_doc, price):
        self.__proced = proced
        self.__date = date
        self.__name_doc = name_doc
        self.__price = price

    def get_proced(self):
        return self.__proced
    def get_date(self):
        return self.__date
    def get_name_doc(self):
        return self.__name_doc
    def get_price(self):
        return self.__price

    def __str__(self):
        return (f'''
Процедура: {self.__proced}
Дата: {self.__date}
Врач: {self.__name_doc}
Стоимость: {self.__price}
''')


def Treatment_costs():
    name = input('Имя, фамилия, отчество: ')
    adres = input('Полный адрес: ')
    phone = input('Номер телефона: ')
    second_contact = input('Телефон и имя контактного лица: ')
    patient = Patient(name, adres, phone, second_contact)
    print(patient)

    for i in range(1, 4):
        proced = input('Название процедуры: ')
        date = input('Дата процедуры: ')
        name_doc = input('Фамилия врача: ')
        price = input('Стоимость: ')
        procd = Procedure(proced, date, name_doc, price)
        print(f'Процедура №{i}')
        print(procd)


Treatment_costs()