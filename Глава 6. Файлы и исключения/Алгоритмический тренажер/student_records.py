import os

def add_student_records():
    with open('students.txt', 'w') as out_file:
        while True:
            name = input('Имя студента: ')
            if not name: break
            else: print(name, file=out_file); print(input('Введите оценку: '), file=out_file)

def show_student_records():
    with open('students.txt') as students_file:
        while True:
            name = students_file.readline().rstrip()
            if not name: break
            else:
                eval = float(students_file.readline().rstrip())

                print('Имя студента:', name)
                print('Оценка:', eval)
                print()

def delete_student_record():
    flag = False
    search = input('Kого желаете удалить? ')
    with open('students.txt') as students_file, open('temp.txt', 'w') as temp_file:
        while True:
            name = students_file.readline().rstrip()
            if not name:
                break
            else:
                eval = float(students_file.readline().rstrip())
                if name != search:
                    print(name, file=temp_file); print(eval, file=temp_file)
                else: flag = True

    os.remove('students.txt')
    os.rename('temp.txt', 'students.txt')

    if flag:
        print('Файл обновлен.')
    else:
        print('Этo значение в файле не найдено.')

def modify_student_records():
    flag = False
    search = input('Кого ищите? ')
    with open('students.txt') as students_file, open('temp.txt', 'w') as temp_file:
        while True:
            name = students_file.readline().rstrip()
            if not name: break
            else:
                eval = float(students_file.readline().rstrip())
                if name == search:
                    new_eval = input('Новая оценка: ')
                    print(name, file=temp_file); print(new_eval, file=temp_file); flag = True
                else: print(name, file=temp_file); print(eval, file=temp_file)

    os.remove('students.txt')
    os.rename('temp.txt', 'students.txt')

    if flag: print ('Файл обновлен.')
    else: print('Этo значение в файле не найдено.')


