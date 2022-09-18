import car
SPEED = 5
def main():
    year_mod = input('Год модели: ')
    make = input('Фирма изготовитель: ')
    auto = car.Car(year_mod, make)
    count = 0
    print(f'Скорость {auto.get_speed()}')
    input('Увеличить скорость? ')
    while count < 5:
        auto.accelerate(SPEED)
        print(auto.get_speed())
        input('Увеличить скорость? ')
        count += 1
    count = 0
    print(f'Скорость {auto.get_speed()}')
    input('Уменьшить скорость? ')
    while count < 5:
        auto.stop(SPEED)
        print(auto.get_speed())
        input('Уменьшить скорость? ')
        count += 1



if __name__== '__main__': main()