COIN_5 = 5
COIN_10 = 10
COIN_50 = 50
def Counting_coins():
    quantity_coin_5 = int(input('Количество монет 5 коп.: '))
    total_5 = quantity_coin_5 * COIN_5
    quantity_coin_10 = int(input('Количество монет 10 коп.: '))
    total_10 = quantity_coin_10 * COIN_10
    quantity_coin_50 = int(input('Количество монет 50 коп.: '))
    total_50 = quantity_coin_50 * COIN_50
    total_sum = total_5 + total_10 + total_50
    if total_sum == 100:print('1 руб.')
    else: print(total_sum)


if __name__ == '__main__': Counting_coins = Counting_coins()
