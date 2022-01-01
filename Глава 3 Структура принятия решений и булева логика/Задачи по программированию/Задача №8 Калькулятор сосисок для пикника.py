def Picnic_Sausage_Calculator():
    SAUSAGES = 10
    BUNS = 8
    picnic_participants = int(input('Количество участников пикника: '))
    number_of_hot_dogs = int(input('Количество хот-догов для каждого участника: '))
    total_hot_dogs = picnic_participants * number_of_hot_dogs
    min_sausage_packs = get_sausage_packs(total_hot_dogs, SAUSAGES)
    min_buns_packs = get_buns_packs(total_hot_dogs, BUNS)
    print(f'Минимально необходимое количество упаковок с сосисками - {min_sausage_packs}.')
    print(f'Минимально необходимое количество упаковок с булочками - {min_buns_packs}.')
    print(f'Количество оставшихся сосисок - {(min_sausage_packs * SAUSAGES) - total_hot_dogs}.')
    print(f'Количество оставшихся булочек - {(min_buns_packs * BUNS) - total_hot_dogs}.')

def get_sausage_packs(arg1, arg2):
    sausage_packs = (arg1 + arg2) // arg2
    return sausage_packs

def get_buns_packs(arg1, arg2):
    buns_packs = (arg1 + arg2) // arg2
    return buns_packs

Picnic_Sausage_Calculator()


