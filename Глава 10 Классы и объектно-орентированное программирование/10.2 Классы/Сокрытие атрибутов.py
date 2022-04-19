import random


# Класс Coin имитирует монету, которую можно подбрасывать.
class Coin:
    # Метод  __init__  инициализирует атрибут данных sideup значением 'Орел'.
    def __init__(self):
        self.__sideup = 'Орел'

    # Метод toss генерирует случайное число в диапазоне от 0  до 1.
    # Если это число равно 0, то sideup получает значение 'Орел'.
    # В противном случае sideup получает значение 'Решка'.
    def toss(self):
        if random.randint(0, 1) == 0:
            self.__sideup = 'Орел'
        else:
            self.__sideup = 'Решка'

    # Метод get_sideup возвращает значение, на которое ссыпается sideup.
    def get_sideup(self):
        return self.__sideup


def coin_demo():
    # Создать объект на основе класса Coin.
    my_coin = Coin()
    # Показать обращенную вверх сторону монеты.
    print(f'Эта сторона обращена вверх: {my_coin.get_sideup()}')
    # Подбросить монету.
    print('Подбрасываю монету ... ')
    for count in range(10):
        my_coin.toss()
        my_coin.sideup = 'Рубо' # C __init__ не работает
        # Показать обращенную вверх сторону монеты.
        if my_coin.get_sideup() == 'Орел':
            print("Опять Орел")
        else:
            print("Решка")


coin_demo()
