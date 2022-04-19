class Car:
    def __init__(self, model, make):
        self.__year_model = model
        self.__make = make
        self.___speed = 0

    def accelerate(self,amount):
        self.___speed += amount

    def break_car(self,amount):
        self.___speed -= amount

    def get_year_mode(self):
        return self.__year_model
    def get_make(self):
        return self.__make
    def get_speed(self):
        return self.___speed

    def __str__(self):
        return (f'''
Год выпуска: {self.__year_model}
Фирма изготовитель: {self.__make}
Скорость автомобиля: {self.___speed}''')

def test_car():
    car = Car(input('Год выпуска: '), input("Фирма изготовитель: "))
    print(car)
    count = 1
    speed = 5
    input('Стартуем? ')
    while count < 6:
        car.accelerate(speed)
        print(car)
        input("Добавить газку? ")
        count += 1
    print('Хорош. Теперь збавляем.')
    count = 1
    speed = 5
    input('Збавить скорость? ')
    while count < 6:
        car.break_car(speed)
        print(car)
        input('Еще збавить? ')
        count += 1


test_car()





