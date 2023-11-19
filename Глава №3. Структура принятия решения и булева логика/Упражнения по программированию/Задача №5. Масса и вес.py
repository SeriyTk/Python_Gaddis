def Mass_weight():
    mass = float(input('Масса тела в килограммах: '))
    weight = mass * 9.8
    if weight > 500: print('Тело слишком тяжелое.')
    elif weight < 100: print('Тело слишком легкое.')
    else: print("Вес тела в норме.")



if __name__ == '__main__': Mass_weight = Mass_weight()
