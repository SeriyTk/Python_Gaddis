def Distance_traveled():
    SPEED = 70
    for i in range(3):
        time = int(input('Часы: '))
        print(f'За {time} часов автомобиль пройдет {time * SPEED} км.')


Distance_traveled()
