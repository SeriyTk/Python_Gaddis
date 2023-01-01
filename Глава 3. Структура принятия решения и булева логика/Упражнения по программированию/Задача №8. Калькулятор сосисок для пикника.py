def Picnic_sausage_calculator():
    SAUSAGE = 10
    BUNS = 8
    number_of_picnic_participants = int(input('Количество участников пикника: '))
    number_of_hot_dogs = int(input('Количество хот-догов: '))
    total_hot_dogs = number_of_picnic_participants * number_of_hot_dogs
    min_sausage = total_hot_dogs // SAUSAGE
    if total_hot_dogs % SAUSAGE != 0: print(f'Количество упаковок с сосисками {min_sausage + 1}')
    else: print(f'Количество упаковок с сосисками {min_sausage }')

    min_buns = total_hot_dogs // BUNS
    if total_hot_dogs % BUNS != 0: print(f'Количество упаковок с булочками {min_buns + 1}')
    else: print(f'Количество упаковок с булочками {min_buns}')

    if total_hot_dogs % SAUSAGE != 0: print(f'Количество оставшихся сосисок {(min_sausage + 1) * SAUSAGE - total_hot_dogs}')
    else: print(f'Количество оставшихся сосисок {min_sausage * SAUSAGE - total_hot_dogs}')
    if total_hot_dogs % BUNS != 0: print(f'Количество оставшихся булочек {(min_buns + 1) * BUNS - total_hot_dogs}')
    else: print(f'Количество оставшихся булочек {min_buns * BUNS - total_hot_dogs}')


Picnic_sausage_calculator()