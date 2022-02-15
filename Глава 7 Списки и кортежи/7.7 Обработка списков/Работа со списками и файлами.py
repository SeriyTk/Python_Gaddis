def write_list():
    cities = ['Нью-Йорк', 'Бостон', 'Атланта', 'Даллас']
    with open(r'G:\cities.txt', 'w') as cities_file:
        for citi in cities:
            print(citi, file=cities_file)
    print('Данные в файл занесены.')


def read_list():
    with open(r'G:\cities.txt') as cities_file:
        for citi in cities_file:
            print(citi.rstrip())

read_list()
