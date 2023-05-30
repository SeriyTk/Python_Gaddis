import random as rnd
class Coin:
    # Метод init инициализирует атрибут данных sideup значением 'Орел'.
    def __init__(self): self.__sideup = 'Орел'

    def toss(self):
        if rnd.randint(0, 1) == 0: self.__sideup = 'Орел'
        else: self.__sideup = 'Решка'

    def get_sideup(self): return self.__sideup
    def __str__(self): return f'{self.__sideup}'