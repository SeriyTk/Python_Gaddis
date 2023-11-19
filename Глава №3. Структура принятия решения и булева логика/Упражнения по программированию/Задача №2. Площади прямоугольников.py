def Areas_rectangles():
    length1 = float(input('Длина №1: '))
    width1 = float(input('Ширина №1: '))
    areas1 = length1 * width1

    length2 = float(input('Длина №2: '))
    width2 = float(input('Ширина №2: '))
    areas2 = length2 * width2

    if areas1 > areas2: print('Площадь №1 больше, чем площадь №2.')
    elif  areas2 > areas1: print('Площадь №2 больше, чем площадь №1.')
    else: print('Площади одинаковые.')



if __name__ == '__main__': Areas_rectangles = Areas_rectangles()
