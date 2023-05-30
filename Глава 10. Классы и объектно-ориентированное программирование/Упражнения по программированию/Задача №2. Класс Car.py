class Car:
    def __init__(self, year_model, make):
        self.__year_mode = year_model
        self._make = make
        self.__speed = 0
    def accelerate(self): self.__speed += 5
    def breaks(self): self.__speed -= 5
    def get_speed(self): return self.__speed

def main():
    year_model = input('Год выпуска: ')
    make = input('Фирма изготовитель: ')
    car = Car(year_model, make)
    print(f'Сейчас скорость {car.get_speed()}')
    print('Добавить газку?')
    enter = input('Если да, то - д: ')
    while enter == 'д':
        car.accelerate()
        print(f'Сейчас скорость {car.get_speed()}')
        print('Добавить еще газку?')
        enter = input('Если да, то - д: ')



if __name__ == '__main__': main()
