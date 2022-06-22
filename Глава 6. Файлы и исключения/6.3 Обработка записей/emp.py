def save_emp_records():
    with open('employees.txt', 'w') as emp_file:
        for count in range(int(input('Cкoлькo записей о сотрудниках Вы хотите создать?: '))):
            print(f'Введите данные о сотруднике №{count + 1}')
            print(input('Имя: '), file=emp_file)
            print(input('Идентификационный номер: '), file=emp_file)
            print(input('Отдел: '), file=emp_file)

    print('Записи о  сотрудниках сохранены в ernployees.txt.')

def read_emp_records():
    with open('employees.txt') as emp_file:
        while True:
            name = emp_file.readline().rstrip()
            if not name: break
            else:
                id_num = emp_file.readline().rstrip()
                dept = emp_file.readline().rstrip()

                print(f'Имя: {name}')
                print(f'ИД: {id_num}')
                print(f'Отдел: {dept}')
                print()