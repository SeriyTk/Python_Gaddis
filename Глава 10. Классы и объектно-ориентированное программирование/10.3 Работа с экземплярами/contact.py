import pickle

class Contact:
    def __init__(self, name, phone, email):
        self.__name = name
        self.__phone = phone
        self.__email = email

    def set_name(self, name): self.__name = name
    def set_phone(self, phone): self.__phone = phone
    def set_email(self, email): self.__email = email

    def get_name(self): return self.__name
    def get_phone(self): return self.__phone
    def get_email(self): return self.__email

    def __str__(self):
        return (f'''
Имя: {self.__name}
Телефон: {self.__phone}
Электронная почта: {self.__email}
''')

def load_file(FILENAME):
    try:
        with open(FILENAME, 'rb') as in_file: contact_dct = pickle.load(in_file)
    except IOError: contact_dct = {}
    return contact_dct
def get_menu():
    print()
    print('Меню')
    print("----------------------------------------------------------------------")
    print('1. Найти контактное лицо')
    print('2. Добавить новое контактное лицо')
    print('3. Изменить существующее контактное лицо')
    print('4. Удалить контактное лицо')
    print('5. Выйти из программы')
    print()
    choice = int(input('Введите выбранный пункт: '))
    while choice < 1 or choice > 5:
        choice = int(input('Введите выбранный пункт: '))
    return choice
def look_up(mycontacts):
    name = input('Введите имя: ')
    print(mycontacts.get(name, 'Это имя не найдено.'))
def add(mycontacts):
    name = input('Имя: ')
    phone = input('Телефон: ')
    email = input('Эл.адрес: ')

    entry = contact.Contact(name, phone, email)

    if name not in mycontacts:
        mycontacts[name] = entry
        print('Запись добавлена')
    else:
        print('Это имя существует.')
def change(mycontacts):
    name = input('Введите имя: ')
    if name in mycontacts:
        phone = input('Введите новый телефон: ')
        email = input("Введите новый эл.адрес: ")
        entry = contact.Contact(name, phone, email)

        mycontacts[name] = entry
        print('Информация обновлена.')
    else: print('Это имя не найдено. ')
def delete(mycontacts):
    name = input('Введите имя: ')
    if name in mycontacts: del mycontacts[name]
    else: print('Это имя не найдено.')
def save_contacts(FILENAME, mycontacts):
    with open(FILENAME, 'wb') as out_file: pickle.dump(mycontacts, out_file)