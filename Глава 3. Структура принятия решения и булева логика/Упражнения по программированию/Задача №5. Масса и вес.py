def Mass_and_weight():
    mass = float(input('Масса тела: '))
    weight = mass * 9.8
    print(weight)
    if weight > 500: print('Тело слишком тяжелое.')
    elif weight < 100: print('Тело слишком легкое.')
    else: print("Вес нормальный.")

Mass_and_weight()