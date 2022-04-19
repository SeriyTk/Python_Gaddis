from modules import Employee




def employee():
    emp1 = Employee(input('Введите имя: '), input('id: '), input('Отдел: '), input('Должность: '))
    emp2 = Employee(input('Введите имя: '), input('id: '), input('Отдел: '), input('Должность: '))
    emp3 = Employee(input('Введите имя: '), input('id: '), input('Отдел: '), input('Должность: '))
    print('Имя \t Номер id \t Отдел \t Должность')
    print(f'{emp1.get_name()} \t\t {emp1.get_id()} \t\t {emp1.get_department()} \t\t {emp1.get_position()}')
    print(f'{emp2.get_name()} \t\t {emp2.get_id()} \t\t {emp2.get_department()} \t\t {emp2.get_position()}')
    print(f'{emp3.get_name()} \t\t {emp3.get_id()} \t\t {emp3.get_department()} \t\t {emp3.get_position()}')






employee()