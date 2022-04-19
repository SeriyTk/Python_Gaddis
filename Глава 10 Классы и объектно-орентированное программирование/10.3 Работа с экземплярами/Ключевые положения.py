# Каждый экземплят имеет собственный набор атрибутов данных
import coin
def coin_toss():
    # Создать три объекта класса Coin.
    coin1 = coin.Coin()
    coin2 = coin.Coin()
    coin3 = coin.Coin()

    # Показать повернутую вверх сторону каждой монеты.
    print('Boт три монеты, у которых эти стороны обращены вверх: ')
    print(coin1.get_sideup())
    print(coin2.get_sideup())
    print(coin3.get_sideup())

    # Подбросить монету.
    print('Подбрасываю все три монеты ... ')
    print()
    coin1.toss()
    coin2.toss()
    coin3.toss()

    # Показать повернутую вверх сторону каждой монеты.
    print('Теперь обращены вверх вот эти стороны: ')
    print(coin1.get_sideup())
    print(coin2.get_sideup())
    print(coin3.get_sideup())
    print()


coin_toss()