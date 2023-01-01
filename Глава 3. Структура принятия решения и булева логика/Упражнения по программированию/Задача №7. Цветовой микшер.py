def Color_mixer():
    while True:
        color1 = input('Введите цвет №1: ')
        if color1 != "красный" and color1 != "синий" and color1 != "желтый": print('Введите правильный цвет №1.')
        else:
            color2 = input('Введите цвет №2: ')
            if color2 != "красный" and color2 != "синий" and color2 != "желтый": print('Введите правильный цвет №2.')
            else:
                if (color1 == "красный" and color2 == "синий" or
                    color2 == "красный" and color1 == "синий"): print('Фиолетовый'); break
                elif (color1 == 'красный' and color2 == 'желтый' or
                     color2 == 'красный' and color1 == 'желтый'): print('Оранжевый'); break
                elif (color1 == 'синий' and color2 == 'желтый' or
                     color2 == 'синий' and color2 == 'желтый'): print('Зеленый'); break

Color_mixer()