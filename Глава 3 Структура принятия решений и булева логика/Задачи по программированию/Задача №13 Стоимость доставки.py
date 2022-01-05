def Cost_of_delivery():
    BID1 = 150
    BID2 = 300
    BID3 = 400
    BID4 = 475
    package_weight = int(input('Масса пакета в гр.: '))
    delivery_fee = get_delivery_fee(BID1, BID2, BID3, BID4, package_weight)
    print(f'Вес пакета {package_weight} гр., плата за доставку {delivery_fee} руб.')


def get_delivery_fee(BID1, BID2, BID3, BID4, package_weight):
    if package_weight <= 200:
        delivery_fee = package_weight // 100 * BID1
    elif 200 < package_weight <= 600:
        delivery_fee = package_weight // 100 * BID2
    elif 600 < package_weight <= 1000:
        delivery_fee = package_weight // 100 * BID3
    elif package_weight > 1000:
        delivery_fee = package_weight // 100 * BID4

    return delivery_fee


Cost_of_delivery()
