def test_score_average():
    test1 = float(input('Введите оценку №1: '))
    test2 = float(input('Введите оценку №2: '))
    test3 = float(input('Введите оценку №3: '))
    average = (test1 + test2 + test3) / 3
    print(f'Средний бал составляет {average}')

test_score_average()