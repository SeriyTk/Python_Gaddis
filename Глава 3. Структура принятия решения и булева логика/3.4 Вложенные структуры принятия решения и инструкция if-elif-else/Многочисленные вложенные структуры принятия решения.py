def grade():
    A_SCORE = 90
    B_SCORE = 80
    C_SCORE = 70
    D_SCORE = 60
    while True:
        score = int(input('Ваши балы: '))
        if score >= A_SCORE: print('Уровень - А.')
        else:
            if score >= B_SCORE: print('Уровень - B.')
            else:
                if score >= C_SCORE: print('Уровень - C.')
                else:
                    if score >= D_SCORE: print('Уровень - D.')
                    else: print('Уровень - F.')
        enter = input('Enter если дальше или любую клавишу если стоп: ')
        if enter != '': print('Программа завершена.'); break


grade()