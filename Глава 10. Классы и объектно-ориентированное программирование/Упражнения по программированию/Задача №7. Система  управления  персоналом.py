import employee as empl, pickle
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

FILENAME = 'employee.dat'
def main():
    employee = load_employee()
    while True:
        choice = get_menu_choice()
        if choice == LOOK_UP: look_up(employee)
        elif choice == ADD: add(employee)
        elif choice == CHANGE: change(employee)
        elif choice == DELETE: delete(employee)
        elif choice == QUIT: break
    save_employee(employee)
def load_employee():
    try:
        with open(FILENAME, 'rb') as in_file: employee_dct = pickle.load(in_file)
    except IOError: employee_dct = {}
    return employee_dct
def get_menu_choice():
    print()
    print('Меню')
    print('--------------------------------------------------')
    print('1. Найти сотрудника.')
    print('2. Добавить нового сотрудника.')
    print('3. Изменить имя, отдел и должность существующего сотрудника.')
    print('4. Удалить сотрудника.')
    print('5. Выйти из программы.')
    print()
    choice = int(input('Введите выбранный пункт: '))
    while choice < LOOK_UP or choice > QUIT: choice = int(input('Введите выбранный пункт: '))
    return choice
def look_up(employee): print(employee.get(input('Введите ID: '), 'Это ID не найдено.'))
def add(employee):
    name = input('Имя: ')
    id = input('ID: ')
    dept = input('Отдел: ')
    post = input('Должность: ')
    entry = empl.Employee(name, id, dept, post)
    if name not in employee: employee[id] = entry; print('Запись добавлена.')
    else: print("Это имя уже существует.")
def change(employee):
    id = input('ID: ')
    if id in employee:
        name = input('Введите новое имя: ')
        dept = input('Отдел: ')
        post = input('Должность: ')
        entry = empl.Employee(name, id, dept, post)
        employee[id] = entry
        print('Информация обновлена.')
    else: print('Это имя не найдено.')
def delete(employee):
    id = input('ID: ')
    if id in employee: del employee[id]; print('Запись удалена.')
    else: print('Это имя не найдено.')
def save_employee(employee):
    with open(FILENAME, 'wb') as out_file: pickle.dump(employee, out_file)


if __name__ == '__main__': main()
