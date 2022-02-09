import os


def write_students_list():
    with open(r'G:\students.txt', 'a') as file_students:
        while True:
            print(input('Введите имя студента: '), file=file_students)
            print(input('Введите оценку студента: '), file=file_students)
            if input('Если хотите продожлить введите - д: ') != 'д':
                print('Записть в файл занесена.')
                break





def read_students_list():
    with open(r'G:\students.txt') as file_students:
        name = file_students.readline()
        while name != '':
            value = int(file_students.readline())
            name = name.rstrip()
            print(f'Имя студента: {name}.')
            print(f'Оценка: {value}.')
            name = file_students.readline()


read_students_list()


def delete_students_list():
    with open(r'G:\students.txt') as file_students, open(r'G:\temp.txt', 'w') as file_temp:
        flag = False
        search = input('Кого хотите удалить из списка? ')
        name = file_students.readline()
        while name != '':
            value = file_students.readline()
            name = name.rstrip()
            value = value.rstrip()
            if name != search:
                print(name, file=file_temp)
                print(value, file=file_temp)
            else:
                flag = True
            name = file_students.readline()

    os.remove(r'G:\students.txt')
    os.rename(r'G:\temp.txt', r'G:\students.txt')
    if flag:
        print('Имя найдено и удалено.')
    else:
        print('Такого студента нет.')

def modified_students_list():
    with open(r'G:\students.txt') as file_students, open(r'G:\temp.txt', 'w') as file_temp:
        flag = False
        search_name = input('Имя студента: ')
        new_value = input('Новая оценка: ')
        name = file_students.readline()
        while name != '':
            value = file_students.readline()
            name = name.rstrip()
            value = value.rstrip()
            if search_name == name:
                print(name, file=file_temp)
                print(new_value, file=file_temp)
                flag = True
            else:
                print(name, file=file_temp)
                print(value, file=file_temp)
            name = file_students.readline()

    os.remove(r'G:\students.txt')
    os.rename(r'G:\temp.txt', r'G:\students.txt')
    if flag:
        print(f'Оценка у студента {search_name} изменена.')
    else:
        print(f'Студента {search_name} в списке нет.')

modified_students_list()




