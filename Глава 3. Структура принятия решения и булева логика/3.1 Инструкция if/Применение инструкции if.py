def test_average():
    number_ratings = int(input('Количество оценок: '))
    total_ratings = 0
    for number in range(number_ratings):
        rating = int(input(f'Получить оценку №{number + 1}: '))
        total_ratings += rating

    average = total_ratings / number_ratings
    if average > 95: print('Поздравляю.')
    else: print(f'{average:.1f}')

test_average()