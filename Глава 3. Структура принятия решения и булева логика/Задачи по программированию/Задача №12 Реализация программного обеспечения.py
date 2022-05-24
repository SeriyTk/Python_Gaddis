PRICE = 99


def Software_Implementation():
    quantity_of_goods = int(input('Количество: '))
    price_goods = quantity_of_goods * PRICE
    if 10 <= quantity_of_goods <= 19: discount = price_goods * 0.1
    elif 20 <= quantity_of_goods < 50: discount = price_goods * 0.2
    elif 50 <= quantity_of_goods < 100: discount = price_goods * 0.3
    elif 100 <= quantity_of_goods: discount = price_goods * 0.4


    print(F'Сумма скидки {discount}, сумма покупки после вычета скидки {price_goods - discount}')




Software_Implementation()
