def Color_mixer():
    color1 = input('Введите название цвета №1- красный, синий, желтый: ')
    color2 = input('Введите название цвета №2 -  красный, синий, желтый: ')
    while (color1 != 'красный' and color1 != 'синий' and color1 != 'желтый' and
           color2 != 'красный' and color2 != 'синий' and color2 != 'желтый'):
        print('Цвет не корректный.')
        color1 = input('Введите название цвета красный, синий, желтый: ')
        color2 = input('Введите название цвета красный, синий, желтый: ')
    else:
        if color1 == 'красный' and color2 == 'синий' or color2 == 'красный' and color1 == 'синий':
            print('Получается фиолетовый.')
        elif color1 == 'красный' and color2 == 'желтый' or color2 == 'красный' and color1 == 'желтый':
            print('Получается оранжевый.')
        elif color1 == 'синий' and color2 == 'желтый' or color2 == 'синий' and color1 == 'желтый':
            print("Получается зеленый.")
Color_mixer()