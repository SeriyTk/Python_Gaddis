G = 9.8

def falling_distance(time):
    print('Время\tДистанция')
    for t in range(1, time + 1):
        d = 1 / 2  * G * t ** 2
        print(f'{t}\t\t\t{d:.2f}')
falling_distance(10)