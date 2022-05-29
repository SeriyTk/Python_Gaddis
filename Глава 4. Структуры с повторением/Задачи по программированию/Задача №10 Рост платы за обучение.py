START = 45000
STEP = 0.03


def Fee_growth():
    print('Год\t  Сумма')
    for year in range(6): print(f'{year}   \t  {START + (START * STEP) * year}')


Fee_growth()
