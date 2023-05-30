class Patient:
    def __init__(self, initials, adres, phone, last_phone):
        self.__initials = initials
        self.__adres = adres
        self.__phone = phone
        self.__last_phone = last_phone

    def set_initials(self,initials): self.__initials = initials
    def set_adres(self,adres): self.__adres = adres
    def set_phone(self, phone): self.__phone = phone
    def set_last_phone(self, last_phone): self.__last_phone = last_phone

    def get_initials(self): return self.__initials
    def get_adres(self): return self.__adres
    def get_phone(self): return self.__phone
    def get_last_phone(self): return self.__last_phone

    def __str__(self): return f'''
Фамилия, имя, отчество: {self.__initials};
адрес, город, область и почтовый индекс: {self.__adres};
телефонный номер: {self.__phone}
имя и телефон контактного лица для экстренной связи: {self.__last_phone}
'''
class Procedure:
    def __init__(self, title, date, name, price):
        self.__title = title
        self.__date = date
        self.__name = name
        self.__price = price

    def set_title(self, title): self.__title = title
    def set_date(self, date): self.__date = date
    def set_name(self, name): self.__name = name
    def set_price(self, price): elf.__price = price

    def get_title(self): return self.__title
    def get_date(self): return self.__date
    def get_name(self): return self.__name
    def get_price(self): return self.__price

    def __str__(self): return f'''
Название процедуры: {self.__title}
Дата: {self.__date}
Врач: {self.__name}
Стоимость: {self.__price}
'''