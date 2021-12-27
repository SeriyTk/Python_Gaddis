def test_aveгage():
    HIGH_SCORE = 95
    average_mark = get_average_mark()
    print(f'Средний бал составляет {average_mark}.')
    if average_mark > HIGH_SCORE:
        print('Поздравляем!!!')


def get_average_mark():
    sum_testes = 0
    total = 0

    for number in range(3):
        test = int(input(f'Введите оценку № {number + 1}: '))
        sum_testes += test
        total += 1

    return sum_testes / total

test_aveгage()

