def display_menu():
    print('Меню.')
    print('1. Отыскать день рождения.')
    print('2. Добавить новый день рождения.')
    print('3. Изменить день рождения.')
    print('4. Удалить день рождения.')
    print('5. Выйти из программы.')

def add_birthdays(birthdays):
    while True:
        name = input('Введите имя: ')
        bday = input('Введите день рождения: ')
        if name not in birthdays:
            birthdays[name] = bday
        else:
            print('Этa запись уже существует.')
        enter = input('Хотите сделать еще одну запись введите "д", а иначе любое значение: ')
        if enter != 'д':
            print("Запись завершена.")
            break

def look_up_birthdays(birthdays):
    print(birthdays.get(input('Введите имя: '), "Такого имени не найдено."))

def change_birthdays(birthdays):
    name = input('Введите имя: ')
    while name not in birthdays:
        print('Такого имени нет.')
        name = input('Введите другое имя: ')
    else:
        while name in birthdays:
            bday = input('Введите новую дату дня рождения: ')
            birthdays[name] = bday
            enter = input('Хотите найти еще одно имя введите "д", а иначе любое значение: ')
            if enter == 'д':
                name = input('Введите имя: ')
            else:
                print("Запись завершена.")
                break

def delete_birthdays(birthdays):
    name = input('Введите имя: ')
    while name not in birthdays:
        print('Такого имени нет.')
        name = input('Введите другое имя: ')
    else:
        while name in birthdays:
            del birthdays[name]
            enter = input('Хотите удалить еще одно имя введите "д", а иначе любое значение: ')
            if enter == 'д':
                name = input('Введите имя: ')
            else:
                print("Программа завершена.")
                break


def birthdays():
    display_menu()
    birthdays = {}
    while True:
        choise = int(input('Выберите вариант от 1 до 5: '))
        if 0 == choise or choise> 5:
            print("Неверное значение.")
        else:
            if choise == 1:
                look_up_birthdays(birthdays)
            elif choise == 2:
                add_birthdays(birthdays)
            elif choise == 3:
                change_birthdays(birthdays)
            elif choise == 4:
                delete_birthdays(birthdays)
            elif choise == 5:
                print('Программа завершена.')
                break


birthdays()
