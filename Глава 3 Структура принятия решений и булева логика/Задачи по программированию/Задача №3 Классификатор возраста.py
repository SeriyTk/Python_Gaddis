def Age_classifier():
    persons_age = int(input('Введите возвраст человека: '))
    if persons_age <= 1:
        print('Человек младенец.')
    elif 1 < persons_age < 13:
        print('Человек ребенок.')
    elif 13 <= persons_age < 20:
        print('Человек подросток.')
    else:
        print('Человек взрослый.')

Age_classifier()
