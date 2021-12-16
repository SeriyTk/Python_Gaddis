def test_score_average():
    sum_score = 0
    total_score = 0
    amount_score = int(input('Количество оценок: '))
    for i in range(amount_score):
        score = float(input(f'Введите оценку № {i + 1}: '))
        sum_score += score
        total_score += 1

    score_average = sum_score / total_score
    print(f'Средний бал составляет {score_average}.')

test_score_average()
