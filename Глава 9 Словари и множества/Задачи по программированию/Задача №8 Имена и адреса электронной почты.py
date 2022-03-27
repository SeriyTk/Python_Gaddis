import pickle
def picl_dct():
    print('Делаем словарь.')
    name_mail = {}
    with open(r'G:\n_m.dat', 'wb') as out_n_m:
        while True:
            name = input('Введите имя: ')
            name_mail[name] = input('Введите имя адреса электронной почты: ') + '@mail.com'
            pickle.dump(name_mail, out_n_m)
            enter = input('Хотите продолжить д/н: ')
            if enter.lower() != 'д':
                print("Данные занесены.")
                break


def unpickle_dct():
    with open(r'G:\n_m.dat', 'rb') as input_n_m:
        dct = pickle.load(input_n_m)
        return dct


def display_menu():
    print("Меню.")
    print("0. Завершение работы.")
    print("1. Отыскать адрес электронной почты человека.")
    print("2. Добавить новое имя и адрес электронной почты")
    print("3. Изменить существующий адрес электронной почты")
    print("4. Удалить существующее имя и адрес электронной почты")



def get_mail(dct):
    while True:
        search_name = input('Кого ищете? ').lower()
        e_mail = dct.get(search_name, 'такого нет')
        print(f'Адрес электронной почты {search_name} : {e_mail}.')
        enter = input('Хотите продолжить д/н: ')
        if enter.lower() != 'д':
            print("Данные добавлены.")
            break
def add_new(dct):
    while True:
        new_name = input('Введите новое имя: ')
        dct[new_name] = input('Введите имя адреса электронной почты: ') + '@mail.com'
        enter = input('Хотите продолжить д/н: ')
        if enter.lower() != 'д':
            print("Данные добавлены.")
            break
    return dct

def change_mail(dct):
    while True:
        search_name = input('У кого изменить адрес электронной почты? ').lower()
        e_mail = dct.get(search_name, 'такого нет')
        print(f'Адрес электронной почты {search_name} : {e_mail}.')
        dct[search_name] = input('Введите новый адрес электронной почты: ') + '@mail.com'
        enter = input('Хотите продолжить д/н: ')
        if enter.lower() != 'д':
            print(f"Данные изменены.")
            break
    return dct

def del_item(dct):
    while True:
        name = input('Кого хотите удалить? ')
        dct = dct.pop(name, 'Такого нет.')
        enter = input('Хотите продолжить д/н: ')
        if enter.lower() != 'д':
            print("Данные удалены.")
            break
    return dct

def Names_and_email_addresses():
    #dct = picl_dct()
    dct = unpickle_dct()
    display_menu()
    while True:
        enter = int(input('Введите желаемое действие (1 - 4) либо 0, чтобы завершить работу: '))
        if enter == 0:
            print('Работа завершена.')
            break
        else:
            while  enter > 4:
                print('Такого пункта нет.')
                enter = int(input('Введите желаемое действие (1 - 4): '))
            else:
                if enter == 1:
                    get_mail(dct)
                elif enter == 2:
                    add_new(dct)
                elif enter == 3:
                    change_mail(dct)
                elif enter == 4:
                    del_item(dct)


Names_and_email_addresses()
