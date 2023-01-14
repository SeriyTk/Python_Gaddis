def Distance_traveled():
    speed = int(input('Какая скорость транспортного средства в км/ч? '))
    hours = int(input('Сколько часов оно двигалось? '))
    print('Час\tПройденное расстояние')
    print('-----------------------------------')
    for hour in range(1, hours + 1): print(f'{hour} \t\t {speed * hour}')

Distance_traveled()