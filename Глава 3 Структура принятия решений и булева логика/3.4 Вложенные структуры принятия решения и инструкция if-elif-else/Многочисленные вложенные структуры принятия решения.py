def grader():
    A = 90
    B = 80
    C = 70
    D = 60
    score = int(input('Введите оценку: '))
    if score >= A:
        print('Ваш уровень А.')
    else:
        if score >= B:
            print('Ваш уровень B.')
        else:
            if score >= C:
                print('Ваш уровень C.')
            else:
                if score >= D:
                    print('Ваш уровень D.')
                else:
                    print('Ваш уровень E.')


grader()
