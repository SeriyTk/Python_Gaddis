import coin

def coin_argument():
    # Создать объект Coin.
    my_coin = coin.Coin()

    # Эта инструкция покажет 'Орел'.
    print(my_coin.get_sideup())

    # Передать объект в функцию flip.
    coin.flip(my_coin)

    # Эта инструкция может показать 'Орел' либо'Решка'.
    print(my_coin.get_sideup())



coin_argument()
