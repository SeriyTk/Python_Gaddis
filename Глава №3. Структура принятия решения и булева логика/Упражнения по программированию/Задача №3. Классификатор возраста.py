def Age_classifier():
    age = int(input('Введите возрасть: '))
    if age <= 1: print('Младенец.')
    elif 1 < age  < 13: print('Ребенок.')
    elif 13 <= age < 20: print('Подросток.')
    else: print("Взрослый.")



if __name__ == '__main__': Age_classifier = Age_classifier()
