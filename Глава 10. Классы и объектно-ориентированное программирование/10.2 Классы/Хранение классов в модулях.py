import coin

def main():
    # Создать объект на основе класса Coin.
    my_coin = coin.Coin()
    # Показать обращенную вверх сторону монеты.
    print(f'Эта сторона обращена вверх: {my_coin.get_sideup()}')
    # Подбросить монету.
    print('Подбрасываю монету 10 раз... ')
    for count in range(10): my_coin.toss(); print(my_coin.get_sideup())


main()
