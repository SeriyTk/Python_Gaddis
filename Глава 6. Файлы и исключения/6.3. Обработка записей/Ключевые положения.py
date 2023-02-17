'''Сохраненные в файле данные часто организованы в виде записей. Запись - это полный
набор данных об объекте, а поле - это отдельная порция данных в записи.'''
def save_emp_records():
    num_emps = int(input('Cкoлькo записей о сотрудниках Вы хотите создать? '))
    with open('employees.txt', 'w') as emp_file:
        for count in range(num_emps):
            print(f'Bвeдитe данные о сотруднике № {count + 1}')
            name = input('Имя: ')
            id_num = input('Идентификационный номер: ')
            dept = input('Отдел: ')

            emp_file.write(f'{name}\n ')
            emp_file.write(f'{id_num}\n')
            emp_file.write(f'{dept}\n')
            print()

    print('Записи о сотрудниках сохранены в employees.txt.')


    if __name__ == '__main__': save_emp_records()
print()
def read_emp_record():
    with open('employees.txt') as emp_file:
        print('Вот список сотрудников')
        print()
        while True:
            name = emp_file.readline().rstrip()
            if name == '':  break
            else:
                id_num = emp_file.readline().rstrip()
                dept = emp_file.readline().rstrip()

                print (f'Имя: {name}')
                print(f'ID: {id_num}')
                print(f'Oтдeл: {dept}')
                print()

if __name__ == '__main__': read_emp_record()

