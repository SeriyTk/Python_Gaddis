import pickle

class Contact:
    def __init__(self, name, phone, email):
        self.__name = name
        self.__phone = phone
        self.__email = email

    def set_name(self,name):
        self.__name = name
    def set_phone(self,phone):
        self.__phone = phone
        def set_email(self,email):
            self.__email = email

    def get_name(self):
        return self.__name
    def get_phone(self):
        return self.__phone
    def get_email(self):
        return self.__email

    def __str__(self):
        return (f'''
Имя: {self.__name}
Телефон: {self.__phone}
Электронная почта: {self.__email}
''')

def chois_menu():
    print("Пункты меню:")
    print("1.Найти контакт")
    print("2.Добавить контакт")
    print("3.Заменить контакт")
    print("4.Удалить контакт")
    print("5.Завершить")
    print()
    chois = int(input('Выберите пунк меню: '))
    while chois < 1 or chois > 5:
        print('Такого пункта меню нет.')
        chois = int(input('Выберите пунк меню: '))
    return chois

def load_contacts(par):
    try:
        with open(par, 'rb') as input_file:
            contact_dct = pickle.load(input_file)
    except EOFError:
        contact_dct = {}
    return contact_dct

def look_up(par):
    name = input('Кого ищете?: ')
    print(par.get(name,'Такого не найдено.'))

def add(par):
    name = input('Имя: ')
    phone = input('Телефон: ')
    email = input('Электронный адрес: ')

    entry = Contact(name, phone, email)

    if name not in par:
        par[name] = entry
        print('Запись добавлена.')
    else:
        print("Такая запись уже есть.")

def change(par):
    name = input('Введите имя: ')
    if name in par:
        phone = input('Новый номер телефона: ')
        email = input('Новый электронный адрес: ')

        entry = Contact(name, phone, email)
        par[name] = entry
        print('Запись обновлена')
    else:
        print("Такого имени нет.")

def delete(par):
    name = input('Введите имя: ')
    if name in par:
        del par[name]
        print("Записть удалена.")
    else:
        print("Такого имени нет.")
        
def save_contacts(par1,par2):
    with open(par1,'wb') as outfile:
        pickle.dump(par2, outfile)
    

