import random as rnd
class Coin:
    # Метод init инициализирует атрибут данных sideup значением 'Орел'.
    def __init__(self): self.sideup = 'Орел'

    def toss(self):
        if rnd.randint(0, 1) == 0: self.sideup = 'Орел'
        else: self.sideup = 'Решка'

    def get_sideup(self): return self.sideup
def main():
    my_coin = Coin()
    print('Этa сторона обращена вверх: ', my_coin.get_sideup())
    print('Подбрасываю монету ... ')
    my_coin.toss()
    print('Этa сторона обращена вверх: ', my_coin.get_sideup())

if __name__ == '__main__': main()