def Color_mixer():
    color1 = input('Красный, синий или желтый: ')
    color2 = input('Красный, синий или желтый: ')
    if ((color1 != 'красный' and color1 != 'синий' and color1 != 'желтый') or
        (color2 != 'красный' and color2 != 'синий' and color2 != 'желтый') or
        color1 == color2): print('Ошибка.')
    elif ((color1 == 'красный' and color2 == 'синий') or
        (color2 == 'красный' and color1 == 'синий')): print('фиолетовый')
    elif ((color1 == 'красный' and color2 == 'желтый') or
          (color2 == 'красный' and color1 == 'желтый')): print('оранжевый')
    elif ((color1 == 'синий' and color2 == 'желтый') or
          (color2 == 'синий' and color1 == 'желтый')): print('зеленый')


if __name__ == '__main__': Color_mixer = Color_mixer()
