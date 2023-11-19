А_SCORE = 90
B_SCORE = 80
C_SCORE = 70
D_SCORE = 60
def grader():
    score = int(input('Bвeдитe свои баллы: '))
    if score >= А_SCORE: print('Ваш уро вень - А.' )
    else:
        if score >= B_SCORE: print('Baш уровень - В.')
        else:
            if score >= C_SCORE: print('Baш уровень - C.')
            else:
                if score >= D_SCORE: print('Baш уровень - D.')
                else: print('Baш уровень - F.')


if __name__ == '__main__': grader = grader()
