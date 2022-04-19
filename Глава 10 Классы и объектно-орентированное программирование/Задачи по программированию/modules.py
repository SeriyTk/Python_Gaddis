import pickle

class Employee:
    def __init__(self, name, id_num, department, position):
        self.__name = name
        self.__id_num = id_num
        self.__department = department
        self.__position = position


    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id_num

    def get_department(self):
        return self.__department

    def get_position(self):
        return self.__position

        def __str__(self):
            return (f'''
    Имя: {self.__name}
    ИД: {self.__id_num}
    Отдел: {self.__department}
    Должность: {self.__position}
    ''')

def chois_menu():
    print('Выберите один из пунков меню:')
    print("1.найти сотрудника в словаре")
    print("2.добавить нового сотрудника в словарь")
    print("3.изменить имя, отдел и должность существующего сотрудника в словаре")
    print("4.удалить сотрудника из словаря")
    print("5.выйти из программы")
    print()
    chois = int(input('Выберите пунк меню: '))
    while chois < 1 or chois > 5:
        print('Такого пункта меню нет.')
        chois = int(input('Выберите пунк меню: '))
    return chois

def load_empt(par):
    try:
        with open(par, 'rb') as input_file:
            empt_dct = pickle.load(input_file)
    except Exception:
        empt_dct = {}
    return empt_dct

def look_up(par):
    name = input('Кого ищете?: ')
    print(par.get(name,'Такого не найдено.'))

def add(par):
    name = input('Имя: ')
    empt = Employee(name, input('id: '), input('Отдел: '), input('Должность: '))

    if name not in par:
        par[name] = entry
        print('Запись добавлена.')
    else:
        print("Такая запись уже есть.")

def change(par):
    name = input('Введите имя: ')
    if name in par:
        name = input('Изменить имя: ')
        id = input('Изменить ИД: ')
        dept = input('Изменить отдел: ')
        pos = input('Изменить должность: ')

        empt = Employee(name, id, dept, pos)
        par[name] = empt
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

def save_empt(par1,par2):
    with open(par1,'wb') as outfile:
        pickle.dump(par2, outfile)


# Для задачи №8
class  Retailltem:
    def __init__(self, descr, amount, price):
        self.__descr = descr
        self.__amount = amount
        self.__price = price


    def   get_descr(self):
        return self.__descr
    def get_amount(self):
        return self.__amount
    def get_amount(self):
        return self.__price

    def __str__(self):
        return (f'''{self.__descr}\t\t{self.__amount}\t\t{self.__price}''')

#class CashRegister:






