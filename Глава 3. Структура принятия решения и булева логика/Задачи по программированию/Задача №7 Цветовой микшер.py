def color_mixer():

    while True:
        color1 = input('Введите цвет №1: ')
        color2 = input('Введите цвет №2: ')
        if (color1 != 'красный' and color1 != 'синий' and color1 != 'желтый' or
        color2 != 'красный' and color2 != 'синий' and color2 != 'желтый'):
            print('Цвет не корректный')
        else:
            if (color1 == 'красный' and color2 == 'синий' or
            color2 == 'красный' and color1 == 'синий'):print('Фиолетовый')
            elif (color1 == 'красный' and color2 == 'желтый' or
            color2 == 'красный' and color1 == 'желтый'): print("Оранжевый")
            elif (color1 == 'синий' and color2 == 'желтый' or
                  color2 == 'синий' and color1 == 'желтый'): print("Зеленый")
            break


color_mixer()