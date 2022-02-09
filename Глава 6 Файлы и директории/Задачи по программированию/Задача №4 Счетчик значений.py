def Value_counter():
    with open(r'G:\students.txt') as f:
        num_name = 0
        name = f.readline()
        while name != '':
            num = f.readline()
            name = f.readline()
            num_name += 1
        return num_name


print(f'Количество имен в списке {Value_counter()}.')
