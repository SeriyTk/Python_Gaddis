def write_list():
    cities = ['Нью-Йорк', 'Бостон', 'Атланта', 'Даллас']
    with open('cities.txt', 'w') as outfile:
        for citi in cities: print(citi, file=outfile)
    print('Файл записан')

def read_list():
    cities = [citi.rstrip() for citi in open('cities.txt')]
    print(cities)