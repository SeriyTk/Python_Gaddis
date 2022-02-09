def write_point():
    with open(r'G:\golf.txt', 'w') as golf:
        enter = 'д'
        while enter == 'д':
            print(input('Введите имя игрока: '), file=golf)
            print(input('Введите счет игрока в игре: '), file=golf)
            enter = input("Если хотите продолжить введите - д, а иначе - любое значение: ")
            if enter != 'д':
                print('Записи в файл внесены.')
                break


def get_point():
    with open(r'G:\golf.txt') as golf:
        name = golf.readline()
        while name != '':
            point = int(golf.readline())
            name = name.rstrip()
            print(name)
            print(point)
            name = golf.readline()


def Points_in_golf():
    
    get_point()


Points_in_golf()
