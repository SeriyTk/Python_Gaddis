'''Цикл, который расположен внуrри еще одного цикла, называется вложенным циклом.'''
for minutes in range(60):
    for seconds in range(60): print(minutes, ': ', seconds)
print()
def test_score_averages():
    num_students = int(input('Cкoлькo у вас студентов? '))
    num_test_scores = int(input('Cкoлькo оценок в расчете на студента? '))
    for student in range(num_students):
        total = 0
        print(f'Студент №{student + 1}: ')
        for test_num in range(num_test_scores):
            print(f'Hoмep лабораторной работы {test_num + 1}', end=' ')
            score = float(input(': '))
            total += score

        average = total / num_test_scores
        print(f'Cpeдний балл студента № {student + 1} составляет: {average:.1f}')
        print()

test_score_averages()