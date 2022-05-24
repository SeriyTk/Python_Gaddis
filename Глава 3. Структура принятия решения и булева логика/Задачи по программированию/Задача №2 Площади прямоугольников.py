def Areas_of_rectangles():
    length1 = int(input('Длина прямоугольника №1: '))
    width1 = int(input("Ширина прямоугольника №1: "))
    length2 = int(input('Длина прямоугольника №2: '))
    width2 = int(input("Ширина прямоугольника №2: "))
    area1 = length1 * width1
    area2 = length2 * width2
    if area1 > area2: print(f"Площадь прямоугольника №1 больше {area1,area2}")
    elif area2 > area1: print(f"Площадь прямоугольника №2 больше {area1,area2}")
    else: print("Прямоугольники одинаковы")


Areas_of_rectangles()
