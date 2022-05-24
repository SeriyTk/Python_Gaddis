HIGH_SCORE = 95


def test_average():
    total_score = 0
    num = 0
    for i in range(3):
        score = int(input(f'Получить оценку за контрольную работу №{i + 1}: '))
        total_score += score
        num += i
    average = total_score / num
    print(f'Средний бал {average}')
    if average >= HIGH_SCORE: print('Поздравляем. Отличный результат!')




test_average()
