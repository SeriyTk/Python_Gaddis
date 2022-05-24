def Mass_and_weight():
    mass = float(input('Масса тела в килограммах: '))
    weigth = mass * 9.8
    print(weigth)
    if weigth > 500: print('Тело слишком тяжелое')
    elif weigth < 100: print('Тело слишком легкое')


Mass_and_weight()