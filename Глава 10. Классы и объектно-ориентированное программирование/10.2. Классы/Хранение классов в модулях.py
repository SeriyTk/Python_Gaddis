import coin
def main():
    my_coin = coin.Coin()
    print('Этa сторона обращена вверх: ', my_coin.get_sideup())
    print('Подбрасываю монету 10 раз: ')
    for i in range(10): my_coin.toss(); print(my_coin.get_sideup())

if __name__ == '__main__': main()