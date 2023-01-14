def Fee_growth():
    START = 145000
    INCREASE = 0.03
    for i in range(6):
        print(f'Плата за год №{i + 1} составляет {START + (START * INCREASE * (i)):,.2f}')

Fee_growth()