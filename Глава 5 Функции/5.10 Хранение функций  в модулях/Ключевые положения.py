from Modules import geometry as geo,menu_options as m_o

ПЛОЩАДЬ_КРУГА = 1
ДЛИНА_КРУГА = 2
ПЛОЩАДЬ_ПРЯМОУГОЛЬНИКА = 3
ПЕРИМЕТР_ПРЯМОУГОЛЬНИК = 4
ВЫХОД = 5
while True:
    m_o.display_menu()
    choise = int(input('Выберите вариант: '))
    if choise == ПЛОЩАДЬ_КРУГА:
        radius = int(input('Введите радиус круга:'))
        print('Площадь круга равна',geo.area_circle(radius))
    elif choise == ДЛИНА_КРУГА:
        radius = int(input('Введите радиус круга:'))
        print('Длина круга равна',geo.circumference(radius))
    elif choise == ПЛОЩАДЬ_ПРЯМОУГОЛЬНИКА:
        a = int(input('Введите ширину прямоугольника: '))
        b = int(input('Введите длину прямоугольника: '))
        print('Площадь прямоугольника равна',geo.area_rectangle(a, b))
    elif choise == ПЕРИМЕТР_ПРЯМОУГОЛЬНИК:
        a = int(input('Введите ширину прямоугольника: '))
        b = int(input('Введите длину прямоугольника: '))
        print('Периметр прямоугольника равна', geo.perimeter_rectangle(a, b))
    elif choise == ВЫХОД:
        print("Программа завершена.")
        break




