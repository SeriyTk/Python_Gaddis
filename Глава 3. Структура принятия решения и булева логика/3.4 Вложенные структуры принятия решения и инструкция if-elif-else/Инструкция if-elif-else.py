def grade():
    A_SCORE = 90
    B_SCORE = 80
    C_SCORE = 70
    D_SCORE = 60
    while True:
        score = int(input('Ваши балы: '))
        if score >= A_SCORE: print('Уровень - А.')
        elif score >= B_SCORE: print('Уровень - B.')
        elif score >= C_SCORE: print('Уровень - C.')
        elif score >= D_SCORE: print('Уровень - D.')
        else: print('Уровень - F.')
        enter = input('Enter если дальше или любую клавишу если стоп: ')
        if enter != '': print('Программа завершена.'); break


grade()