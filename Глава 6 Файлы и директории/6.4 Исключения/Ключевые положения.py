# Исключение  -  это ошибка, которая происходит во время работы программы, приводящая к ее внезапному останову.
# Для корректной обработки исключений используется инструкция try / except.

# try:
        # инструкция
        # инструкция
# except  ИмяИск.лючения:
        # инструкция
        # инструкция
try:
    print(10/0)
except ZeroDivisionError:
    print('На ноль делить нельзя.')

def display_file():
    try:
        filename = input('Название файла: ')
        with open(filename) as coffee_file:
            print(coffee_file.read())
    except IOError:
        print(f'Файла {filename} не существует или неправильный путь.')

display_file()