def Distance_traveled():
    SPEED = 70
    for i in range(int(input('Количество значений: '))):
        time = int(input('Количество часов: '))
        dist = SPEED * time
        print(f'Расстояние которое пройдет автомобиль за {time} часов - {dist} километров.')


Distance_traveled()