def Line_numbers():
    name_file = input('Введите название файла: ')
    with open(name_file) as f:
        num_str = 1
        line = f.readline()
        while line != '':
            print(f'Строка № {num_str}: {line.rstrip()}.')
            num_str += 1
            line = f.readline()


Line_numbers()
