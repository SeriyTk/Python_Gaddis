class Information:
    def __init__(self, name, adres, age, phone_num):
        self.__name = name
        self.__adres = adres
        self.__age = age
        self.__phone_num = phone_num

    def set_name(self, name): self.__name = name
    def set_adres(self, adres): self.__adres = adres
    def set_age(self, age): self.__age = age
    def set_phone_num(self, phone_num): self.__phone_num = phone_num

    def get_name(self): return self.__name
    def get_adres(self): return self.__adres
    def get_age(self): return self.__age
    def get_phone_num(self): return self.__phone_num

    def __str__(self): return f'''
Имя: {self.__name};
адрес: {self.__adres};
возраст: {self.__age};
телефонный номер: {self.__phone_num}.
'''
def main():
    for i in range(3):
        name = input("Введите имя: ")
        adres = input('Адрес: ')
        age = input('Возраст: ')
        phone_num = input("Телефонный номер: ")
        print(Information(name, adres, age, phone_num))

if __name__ == '__main__': main()
