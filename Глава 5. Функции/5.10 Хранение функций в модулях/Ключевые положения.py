import circle, rectangle

AREA_CIRCLE_CHOICE = 1
CIRCUMFERENCE_CHOICE = 2
AREA_RECTANGLE_CHOICE = 3
PERIMETR_RECTANGLE_CHOICE = 4
QUIT_CHOICE = 5

def main():
    while True:
        display_menu()
        choice = int(input('Выберите вариант: '))
        if 1 > choice > 5: continue
        else:
            if choice == AREA_CIRCLE_CHOICE: print(f'Площадь равна {circle.area(float(input("Введите радиус круга: ")))}')
            elif choice == CIRCUMFERENCE_CHOICE: print(f'Длина окружности равна {circle.circumference(float(input("Введите радиус круга: ")))}')
            elif choice == AREA_RECTANGLE_CHOICE: print(f'Площадь равна {rectangle.area(float(input("Bвeдитe ширину прямоугольника: ")), float(input("Bвeдитe длину прямоугольника: ")))}')
            elif choice == PERIMETR_RECTANGLE_CHOICE: print(f'Периметр равен {rectangle.perimetr(float(input("Bвeдитe ширину прямоугольника: ")), float(input("Bвeдитe длину прямоугольника: ")))}')
            elif choice == QUIT_CHOICE: print ('Выходим из программы ... '); break

def display_menu():
    print(f'''
МЕНЮ:
1. Площадь круга
2. Длина окружности
3. Площадь прямоугольника
4. Периметр прямоугольника
5. Выход
''')

main()