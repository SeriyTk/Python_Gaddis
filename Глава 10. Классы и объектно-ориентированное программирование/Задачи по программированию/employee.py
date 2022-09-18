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


def employee_list():
    employee_list = []
    while True:
        if input('Ввести данные? ').lower() != "д": break
        else:
            name = input('Имя: ')
            id_num = input("ИД: ")
            dept = input('Отдел: ')
            job = input("Должность: ")
            employee_list.append(Employee(name, id_num, dept, job))
    return employee_list

def display_employee(employee_list):
    for item in employee_list:
        print(f'''
{item.get_name()} \t\t {item.get_id()} \t\t {item.get_dept()} \t\t {item.get_job()}
''')
'-----------------------------------------------------------------------------------------------'
# №7
def pickle_employee(FILENAМE):
    with open(FILENAМE, 'wb') as out_file:
        while True:
            if input('Ввести данные? ').lower() != "д":
                break
            else:
                name = input('Имя: ')
                id_num = input("ИД: ")
                dept = input('Отдел: ')
                job = input("Должность: ")
                pickle.dump(Employee(name, id_num, dept, job), out_file)
    print(f'Дaнныe записаны в {FILENAМE}')

def load_employee(FILENAМE):
    end_file = False
    with open(FILENAМE, 'rb') as in_file:
        while not end_file:
            try:
                employee_dct = pickle.load(in_file)
                display_data(employee_dct)
            except EOFError: end_file = True; employee_dct = {}
    return employee_dct

def display_data(emloyee):
     print(f'Имя: {emloyee.get_name()}')
     print(f'ИД: {emloyee.get_id()} ')
     print(f'Отдел: {emloyee.get_dept()} ')
     print(f'Должность: {emloyee.get_job()}')
     print ()

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

def look_up(employee_dct): name = input('Введите имя: '); print(employee_dct.get(name, 'Это имя не найдено.'))

def add(employee_dct):
    name = input('Имя: ')
    id_num = input("ИД: ")
    dept = input('Отдел: ')
    job = input("Должность: ")
    entry = Employee(name, id_num, dept, job)
    if name not in employee_dct: employee_dct[name] = entry; print('Запись добавлена.')
    else: print('Этo имя уже существует.')


