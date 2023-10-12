def Growing_grapes():
    ridge_length = float(input('Длина гряды: '))
    end_support = float(input('Пространство, занимаемое концевой опорой: '))
    distance_between_vines = float(input('Расстояние между виноградными лозами: '))
    number_vines = (ridge_length - 2 * end_support) / distance_between_vines
    print(f'''
На гряде длиной {ridge_length} метров поместится {number_vines} виноградных лоз.
''')


if __name__ == '__main__': Growing_grapes = Growing_grapes()
