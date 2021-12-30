def Areas_of_rectangles():
    areas1 = get_areas1()
    areas2 = get_areas2()
    if areas1 > areas2:
        print('Площадь прямоугольника №1 больше, чем площадь прямоугольника №2.')
    elif areas1 < areas2:
        print('Площадь прямоугольника №2 больше, чем площадь прямоугольника №1.')
    else:
        print('Площади прямоугольников одинаковые.')


def get_areas1():
    length = int(input('Длина прямоугольника №1: '))
    width = int(input('Ширина прямоугольника №1: '))
    return length * width


def get_areas2():
    length = int(input('Длина прямоугольника №2: '))
    width = int(input('Ширина прямоугольника №2: '))
    return length * width


Areas_of_rectangles()
