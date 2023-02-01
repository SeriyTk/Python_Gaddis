'''Модуль -
 это файл, который содержит программный код Python. Большие программы
проще отлаживать и поддерживать, когда они подразделены на модули .'''
import Mod
AREA_CIRCLE_CHOICE = 1
CIRCUMFERENCE_CHOICE = 2
AREA_RECTANGLE_CHOICE = 3
PERIMETER_RECTANGLE_CHOICE = 4
QUIT_CHOICE = 5
def geometry():
    Mod.display_menu()
    while True:
        choice = int(input('Выберите вариант: '))
        if choice > 5 or choice < 1: print ('Ошибка: недопустимый выбор. ')
        else:
            if choice == AREA_CIRCLE_CHOICE:
                print(f'Площадь круга равна {Mod.area_circle(float(input("Bвeдитe радиус круга: ")))}.')
            elif choice == CIRCUMFERENCE_CHOICE:
                print(f'Длина окружности равна {Mod.circumferenc_circle(float(input("Bвeдитe радиус круга: ")))}')
            elif choice == AREA_RECTANGLE_CHOICE:
                width = float(input("Bвeдитe щирину прямоугольника: "))
                length = float(input("Bвeдитe длину прямоугольника: "))
                print(f'Площадь прямоугольника равен {Mod.area_rectangle(width, length)}')
            elif choice == PERIMETER_RECTANGLE_CHOICE:
                width = float(input("Bвeдитe щирину прямоугольника: "))
                length = float(input("Bвeдитe длину прямоугольника: "))
                print(f'Периметр прямоугольника равен {Mod.perimeter_rectangle(width, length)}')
            elif choice == QUIT_CHOICE: print ('Выходим из программы ... '); break

if __name__ == '__main__': geometry()