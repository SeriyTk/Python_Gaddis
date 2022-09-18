class Patient:
    def __init__(self, name, adress, phone, sec_phone):
        self.__name = name
        self.__adress = adress
        self.__phone = phone
        self.__sec_phone = sec_phone

    def set_name(self, name): self.__name = name
    def set_adress(self, adress): self.__adress = adress
    def set_phone(self, phone): self.__phone = phone
    def set_sec_phone(self, sec_phone): self.__sec_phone = sec_phone

    def get_name(self): return self.__name
    def get_adress(self): return self.__adress
    def get_phone(self): return self.__phone
    def get_sec_phone(self): return self.__sec_phone
    def __str__(self):return f'''
Информация о пациенте.
-------------------------------------------------------------------------------------
Фамилия, имя, отчество: {self.__name}
Адрес, город, область, индекс: {self.__adress}
Телефонный номер: {self.__phone}
Имя и телефон контактного лица для экстренной связи: {self.__sec_phone}
'''

class Procedure:
    def __init__(self, num, name_proc, date_proc, name_doc, price):
        self.__num = num
        self.__name_proc = name_proc
        self.__date_proc = date_proc
        self.__name_doc = name_doc
        self.__price = price

    def set_num(self, num): self.__num
    def set_name_proc(self, name_proc): self.__name_proc = name_proc
    def set_date_proc(self, date_proc): self.__date_proc = date_proc
    def set_name_doc(self, name_doc): self.__name_doc = name_doc
    def set_price(self, price): self.__price = price

    def get_num(self): return self.__num
    def get_name_proc(self): return self.__name_proc
    def get_date_proc(self): return self.__date_proc
    def get_name_doc(self): return self.__name_doc
    def get_price(self): return self.__price

def proc_list():
    procedure_list = []
    num = 1
    while True:
        if input('Назначить процедуру? ').lower() != "д":
            break
        else:
            name_proc = input('Название процедуры: ')
            date_proc = input('Дата: ')
            name_doc = input('Врач: ')
            price = float(input('Цена: '))
            procedure_list.append(Procedure(num, name_proc, date_proc, name_doc, price))
            num += 1
    return procedure_list

def patient():
    name = input('Имя, отчество и фамилия: ')
    adress = input('Адрес, город, область и почтовый индекс: ')
    phone = input('Телефонный номер: ')
    sec_phone = input('Имя и телефон контактного лица для экстренной связи: ')
    return Patient(name, adress, phone, sec_phone)

def display_list(procedure_list, pat):
    print(pat)
    print('----------------------------------------------------------------------------------')
    for item in procedure_list:
        print(f'''
Процедура №{item.get_num()}
Название процедуры:
{item.get_name_proc()}
Дата: {item.get_date_proc()}
Врач: {item.get_name_doc()}
Стоимость: {item.get_price()}
    ''')