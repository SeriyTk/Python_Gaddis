def Counting_coins_game():
    COINS_5 = 5
    COINS_10 = 10
    COINS_50 = 50
    coins_5 = int(input('Количество монет достоинством в 5 копеек: '))
    coins_10 = int(input('Количество монет достоинством в 10 копеек: '))
    coins_50 = int(input('Количество монет достоинством в 50 копеек: '))
    sum_coins = get_sum_coins(COINS_5, COINS_10, COINS_50, coins_5, coins_10, coins_50)
    if sum_coins == 100:
        print('!!!')
    elif sum_coins > 100:
        print(sum_coins - 100)
    elif sum_coins < 100:
        print(100 - sum_coins)


def get_sum_coins(COINS_5, COINS_10, COINS_50, coins_5, coins_10, coins_50):
    total_5 = COINS_5 * coins_5
    total_10 = COINS_10 * coins_10
    total_50 = COINS_50 * coins_50
    return total_5 + total_10 + total_50


Counting_coins_game()
