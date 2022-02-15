def names_list():
    names = []
    name = input('Введите фамилию: ')
    while name != "хорош":
        names.append(name)
        name = input('Введите следующую фамилию: ')
    else:
        print("Список готов.")
        for item in names:
            print(item)


names_list()
