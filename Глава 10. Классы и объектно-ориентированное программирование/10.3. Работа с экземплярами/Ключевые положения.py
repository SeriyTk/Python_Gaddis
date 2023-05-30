'''Каждый экземпляр класса имеет собственный набор атрибутов данных.'''
import coin
def main():
    coin1 = coin.Coin()
    coin2 = coin.Coin()
    coin3 = coin.Coin()
    print('Boт три монеты, у которых эти стороны обращены вверх:')
    print(coin1)
    print(coin2)
    print(coin3)
    print('Подбрасываю все три монеты ... ')
    print()
    coin1.toss()
    coin2.toss()
    coin3.toss()
    print('Теперь обращены вверх вот эти стороны:')
    print(coin1)
    print(coin2)
    print(coin3)
    print()

if __name__ == '__main__': main()
