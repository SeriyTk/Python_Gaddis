def Distance_traveled(speed, time):
    print('Время\tРасстояние')
    print('-----------------------')
    for hour in range(time):
        distance = (hour + 1) * speed
        print(f'{hour + 1} \t\t \t   {distance}')


km_h = int(input('Скорость км/ч: '))
hours = int(input('Время движения: '))
Distance_traveled(km_h, hours)
