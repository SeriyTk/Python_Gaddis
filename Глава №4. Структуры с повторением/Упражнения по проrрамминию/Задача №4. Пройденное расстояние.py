def Distance_traveled():
    speed = int(input('Какая скорость транспортного средства? '))
    hours = int(input('Сколько часов оно двигалось? '))
    print('Час  Пройденное расстояние')
    print('-----------------------------------')
    for hour in range(hours ): print(f'{hour + 1} \t \t \t {(hour + 1) * speed}')




if __name__ == '__main__': Distance_traveled = Distance_traveled()
