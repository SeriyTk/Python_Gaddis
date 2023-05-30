import contact, pickle

LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

FILENAME = 'contacts.dat'
def main():
    mycontacts = load_contacts()
    while True:
        choice = get_menu_choice()
        if choice == LOOK_UP: look_up(mycontacts)
        elif choice == ADD: add(mycontacts)
        elif choice == CHANGE: change(mycontacts)
        elif choice == DELETE: delete(mycontacts)
        elif choice == QUIT: break
    save_contacts(mycontacts)

def load_contacts():
    try:
        with open(FILENAME, 'rb') as in_file: contact_dct = pickle.load(in_file)
    except IOError: contact_dct = {}
    return contact_dct
def get_menu_choice():
    print()
    print('Меню')
    print('--------------------------------------------------')
    print('1. Найти контактное лицо.')
    print('2. Добавить новое контактное лицо.')
    print('3. Изменить существующее контактное лицо.')
    print('4. Удалить контактное лицо.')
    print('5. Выйти из программы.')
    print()
    choice = int(input('Введите выбранный пункт: '))
    while choice < LOOK_UP or choice > QUIT: choice = int(input('Введите выбранный пункт: '))
    return choice
def look_up(mycontacts): print(mycontacts.get(input('Введите имя: '), 'Это имя не найдено.'))
def add(mycontacts):
    name = input('Имя: ')
    phone = input('Телефон: ')
    email = input('Электронный адрес: ')
    entry = contact.Contact(name, phone, email)
    if name not in mycontacts: mycontacts[name] = entry; print('Запись добавлена.')
    else: print("Это имя уже существует.")
def change(mycontacts):
    name = input('Введите имя: ')
    if name in mycontacts:
        phone = input('Введите новый номер телефона: ')
        email = input('Введите новый электронный адрес: ')
        entry = contact.Contact(name, phone, email)
        mycontacts[name] = entry
        print('Информация обновлена.')
    else: print('Это имя не найдено.')
def delete(mycontacts):
    name = input('Введите имя:')
    if name in mycontacts: del mycontacts[name]; print('Запись удалена.')
    else: print('Это имя не найдено.')
def save_contacts(mycontacts):
    with open(FILENAME, 'wb') as out_file: pickle.dump(mycontacts, out_file)
if __name__ == '__main__': main()
