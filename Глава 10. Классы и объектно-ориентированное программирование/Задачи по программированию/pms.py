import pickle

class Employee:
    def __init__(self, name, id_num, dept, job_title):
        self.__name = name
        self.__id_num = id_num
        self.__dept = dept
        self.__job_title = job_title

    def name(self, name): self.__name = name
    def id(self, id_num): self.__id_num = id_num
    def dept(self, dept): self.__dept = dept
    def job(self, ob_title): self.__job_title = job_title

    def get_name(self): return self.__name
    def get_id(self): return self.__id_num
    def get_dept(self): return self.__dept
    def get_job(self): return self.__job_title

    def __str__(self):return f'''
Имя: {self.__name}
ИД: {self.__id_num}
Отдел: {self.__dept}
Должность: {self.__job_title}
'''

def load_employee(FILENAМE):
    try:
        with open(FILENAМE, 'rb') as in_file: employee_dct = pickle.load(in_file)
    except IOError:employee_dct = {}
    return employee_dct

def get_menu():
    print()
    print('Меню')
    print("------------------------------------------------------------------------------")
    print("1. Найти сотрудника в словаре")
    print("2. Добавить нового сотрудника в словарь")
    print("3. Изменить имя, отдел и должность существующего сотрудника в словаре")
    print("4. Удалить сотрудника из словаря")
    print("5. Выйти из программы")
    print('--------------------------------------------------------------------------------')
    print()
    choice = int(input('Выберите пункт: '))
    while choice < 1 or choice > 5: print("Неверный выбор."); choice = int(input('Выберите пункт: '))
    return choice

def look_up(employee_dct): id_num = input("ИД: "); print(employee_dct.get(id_num, 'Это ИД не найдено.'))

def add(employee_dct):
    name = input('Имя: ')
    id_num = input("ИД: ")
    dept = input('Отдел: ')
    job_title = input("Должность: ")
    entry = Employee(name, id_num, dept, job_title)
    if id_num not in employee_dct: employee_dct[id_num] = entry; print('Запись добавлена.')
    else: print('Этo ИД уже существует.')

def change(employee_dct):
    id_num = input("ИД: ")
    if id_num in employee_dct:
        name = input('Новое имя: ')
        dept = input('Отдел: ')
        job_title = input("Должность: ")
        entry = Employee(name, id_num, dept, job_title)
        employee_dct[id_num] = entry
        print('Информация обновлена.')
    else: print('Такого ИД не найдено.')

def delete(employee_dct):
    id_num = input("ИД: ")
    if name in mycontacts: del employee_dct[id_num]
    else: print('Такого ИД не найдено..')

def save_employee(FILENAME, employee_dct):
    with open(FILENAME, 'wb') as out_file: pickle.dump(employee_dct, out_file)
