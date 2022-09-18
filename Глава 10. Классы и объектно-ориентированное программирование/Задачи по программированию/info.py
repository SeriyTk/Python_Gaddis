class Information:
    def __init__(self, name, address, phone):
        self.__name = name
        self.__address = address
        self.__phone = phone

    def set_name(self, name): self.__name = name
    def set_address(self, address): self.__address = address
    def set_phone(self, phone): self.__phone = phone

    def get_name(self): return self.__name
    def get_address(self): return self.__address
    def get_phone(self): return self.__phone

    def __str__(self): return f'''
Имя: {self.__name}
Адрес: {self.__address}
Телефон: {self.__phone}
'''

def personal_data():
    name = input('Имя: ')
    address = input('Адрес: ')
    phone = input('Номер телефоно: ')
    return name, address, phone