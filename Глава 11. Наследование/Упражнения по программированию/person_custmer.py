class Person:
    def __init__(self, name, adres, phone):
        self.__name = name
        self.__adres = adres
        self.__phone = phone

    def set_name(self, name): self.__name = name
    def set_adres(self, adres): self.__adres = adres
    def set_phone(self, phone): self.__phone = phone

    def get_name(self): return self.__name
    def get_adres(self): return self.__adres
    def get_phone(self): return self.__phone

class Custmer(Person):
    def __init__(self, name, adres, phone, num_client):
        Person.__init__(self, name, adres, phone)
        self.__num_client = num_client

    def set_num_client(self, num_client): self.__num_client = num_client

    def get_num_client(self): return self.__num_client
