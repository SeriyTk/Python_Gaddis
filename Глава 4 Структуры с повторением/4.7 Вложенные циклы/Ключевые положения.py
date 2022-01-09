# Цикл, который расположен внутри еще одного цикла, называется вложенным циклом.
#for hours in range(24):
    #for minutes in range(60):
        #for seconds in range(60):
            #print(f'{hours}:{minutes}:{seconds}')




def test_score_averages():
    num_students = int(input('Количество студентов: '))
    num_scores = int(input(f'Количество оценок студента: '))
    get_average(num_students, num_scores)


def get_average(num_students, num_scores):
    for student in range(num_students):
        total = 0
        print(f'Студент №{student + 1}')
        print()
        for score in range(num_scores):
            test_score = int(input(f'Оценка №{score + 1}: '))
            total += test_score
        average = total / num_scores
        print(f'Средний бал студента №{student + 1} будет {average:.1f}.')
        print('-----------------------------------------------------------------------')
        

test_score_averages()


