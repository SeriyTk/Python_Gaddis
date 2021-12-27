def grader():
    A = 90
    B = 80
    C = 70
    D = 60
    score = int(input('Введите оценку: '))
    if score >= A:
        print('Ваш уровень А.')
    elif score >= B:
        print('Ваш уровень B.')
    elif score >= C:
        print('Ваш уровень C.')
    elif score >= D:
        print('Ваш уровень D.')
    else:
        print('Ваш уровень E.')


grader()
