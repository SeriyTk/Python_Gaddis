def Age_classifier():
    age = int(input('Введите возраст: '))
    if 0 < age <= 1: print('Младенец.')
    elif 1 < age < 13: print('Ребенок.')
    elif 13 <= age < 20: print('Подросток.')
    else: print('Взрослый.')
Age_classifier()