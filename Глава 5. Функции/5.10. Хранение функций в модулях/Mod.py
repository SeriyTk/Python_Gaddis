import math as m

'''Меню'''
def display_menu():
    print(' МЕНЮ')
    print('1. Площадь круга')
    print('2. Длина окружности')
    print('3. Площадь прямоугольника')
    print('4. Периметр прямоугольника')
    print('5. Выход')
'''Круг'''
def area_circle(radius): return m.pi * radius ** 2
def  circumferenc_circle(radius): return 2 * m.pi * radius
'''Прямоугольник'''
def area_rectangle(width, length): return width * length
def perimeter_rectangle(width, length): return 2 * (width + length)

