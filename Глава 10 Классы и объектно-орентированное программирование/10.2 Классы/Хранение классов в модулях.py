import coin


def coin_toss():
    # Создать объект на основе класса Coin.
    my_coin = coin.Coin()
    # Показать обращенную вверх сторону монеты.
    print(f'Эта сторона обращена вверх: {my_coin.get_sideup()}')
    # Подбросить монету.
    print('Подбрасываю монету ... ')
    for count in range(10):
        my_coin.toss()
        # Показать обращенную вверх сторону монеты.
        if my_coin.get_sideup() == 'Орел':
            print("Опять Орел")
        else:
            print("Решка")


coin_toss()
