'''
Цикл, который расположен внутри еще одного цикла, называется вложенным циклом.
'''
def time():
    for hours in range(24):
        for minutes in range(60):
            for seconds in range(60):
                print(f'{hours} : {minutes} : {seconds}')


def test_score_averages():
    num_students = int(input('Количество студентов: '))
    num_test_scores = int(input('Количество оценок каждого студента: '))
    for stud in range(num_students):
        total = 0
        print(f'Оценки студента №{stud + 1}: ')
        for num_test in range(num_test_scores):
            score = int(input(f'Оценка №{num_test + 1}: '))
            total += score

        average = total / num_test_scores
        print(f'Средний бал студента №{stud + 1} составляет {average:.1f}')



test_score_averages()