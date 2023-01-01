def Areas_of_rectangles():
    length1 = int(input('Длина №1: '))
    width1 = int(input('Ширина №1: '))
    length2 = int(input('Длина №2: '))
    width2 = int(input('Ширина №2: '))
    area1 = length1 * width1
    area2 = length2 * width2
    if area1 > area2 : print('Площадь №1 больше.')
    elif area2 > area1 : print('Площадь №2 больше.')
    else: print("Площади одинаковы.")

Areas_of_rectangles()