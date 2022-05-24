A_SCORE = 90
B_SCORE = 80
C_SCORE = 70
D_SCORE = 60
def graber():
    score = int(input('Ваша оценка: '))
    if score >= A_SCORE: print('Ваш уровень - А.')
    else:
        if score >= B_SCORE: print ('Ваш уровень - В.')
        else:
            if score >= C_SCORE: print ('Ваш уровень - С.')
            else:
                if score >= D_SCORE: print ('Ваш уровень - D.')
                else: print ('Ваш уровень - F. ')


graber()