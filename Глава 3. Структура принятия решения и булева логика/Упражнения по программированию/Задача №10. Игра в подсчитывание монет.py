def coin_counting_game():
    total_coins = 0
    while True:
        coin = int(input('Ввести монету достоинством 5, 10 и 50 копеек: '))
        if coin != 5 and coin != 10 and coin != 50: print('Таких монет нет.')
        else:
            total_coins += coin
            enter = input('Ввести еще монету? ')
            if enter != '': break
    if total_coins == 100: print('Приз!!!')
    else:
        if total_coins < 100: print(f'Сумма {total_coins}коп. меньше рубля.')
        else: print(f'Сумма {total_coins}коп. больше рубля.')


coin_counting_game()