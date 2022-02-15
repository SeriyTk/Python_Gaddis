def list_append():
    names_list = []
    while True:
        names_list.append(input('Введите имя: '))
        print('Желаете добавить еще одно имя?')
        answer = input('Введите д если да: ')
        if answer != 'д':
            print("Список создан.")
            break
    for name in names_list:
        print(name)

list_append()
