import random as rnd
class Coin:
    # Метод init инициализирует атрибут данных sideup значением 'Орел'.
    def __init__(self): self.__sideup = 'Орел'

    def toss(self):
        if rnd.randint(0, 1) == 0: self.__sideup = 'Орел'
        else: self.__sideup = 'Решка'

    def get_sideup(self): return self.__sideup
def main():
    my_coin = Coin()
    print('Этa сторона обращена вверх: ', my_coin.get_sideup())
    print('Подбрасываю монету 10 раз: ')
    for i in range(10): my_coin.toss(); print(my_coin.get_sideup())

if __name__ == '__main__': main()