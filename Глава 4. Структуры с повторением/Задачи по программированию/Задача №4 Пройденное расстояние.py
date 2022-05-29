def Distance_traveled():
    speed = int(input('Скорость транспортного средства: '))
    times = int(input('Количество часов: '))
    print("Час\tРасстояние")
    print('---------------------')
    for time in range(times): print(f'{time + 1}    \t    {speed * (time + 1)}')


Distance_traveled()
