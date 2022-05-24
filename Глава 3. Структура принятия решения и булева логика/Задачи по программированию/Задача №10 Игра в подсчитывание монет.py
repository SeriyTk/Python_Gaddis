def coin_counting():
    number_of_coins = int(input("Количество монет: "))
    total_sum = 0
    for coin in range(number_of_coins):
        print('Введите монеты достоинством 5, 10, 50 копеек.')
        coin_denomination = int(input(f'Достоинсво монеты №{coin + 1}: '))
        total_sum += coin_denomination

    if total_sum == 100: print('Поздравляю! Вы выиграли 1 рубль')
    else:
        if total_sum > 100: print('Сумма больше, чем 1 рубль.')
        else: print("Сумма меньше, чем 1 рубль.")


coin_counting()