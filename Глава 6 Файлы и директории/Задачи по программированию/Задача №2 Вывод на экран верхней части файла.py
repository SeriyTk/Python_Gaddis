def Displaying_file():
    name_file = input('Введите название файла: ')
    with open(name_file) as f:
        num_str = 0
        line = f.readline()
        while line != '':
            if num_str <= 4:
                print(int(line))
            num_str += 1
            line = f.readline()


Displaying_file()