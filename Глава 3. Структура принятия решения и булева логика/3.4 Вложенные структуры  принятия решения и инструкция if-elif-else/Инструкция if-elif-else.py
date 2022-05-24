'''
if условие_ 1:
    инструкция
    инструкция
elif условие_2:
    инструкция
    инструкция
Вставить столько выражений elif, сколько нужно:
else:
    инструкция
    инструкция
'''

A_SCORE = 90
B_SCORE = 80
C_SCORE = 70
D_SCORE = 60
def graber():
    score = int(input('Ваша оценка: '))
    if score >= A_SCORE: print('Ваш уровень - А.')
    elif score >= B_SCORE: print('Ваш уровень - В.')
    elif score >= C_SCORE: print('Ваш уровень - С.')
    elif score >= D_SCORE: print('Ваш уровень - D.')
    else: print('Ваш уровень - F. ')

graber()


