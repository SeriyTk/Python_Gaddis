SAUSAGE_PACKAGING = 10
BUN_PACKAGING = 8

def Picnic_Calculator():
    picnic_participants = int(input("Количество участников пикника: "))
    number_h_d = int(input("Количество хот-догов каждому: "))
    total_h_d = picnic_participants * number_h_d
    if (total_h_d % SAUSAGE_PACKAGING) != 0:
        min_sausage_pack = (total_h_d + SAUSAGE_PACKAGING) // SAUSAGE_PACKAGING
    else: min_sausage_pack = total_h_d // SAUSAGE_PACKAGING

    if (total_h_d % BUN_PACKAGING) != 0:
        min_bun_pack = (total_h_d + BUN_PACKAGING) // BUN_PACKAGING
    else: min_bun_pack = total_h_d // BUN_PACKAGING

    print(f'''
Минимально необходимое количество упаковок с сосисками {min_sausage_pack};
минимально необходимое количество упаковок с булочками {min_bun_pack};
количество оставшихся сосисок {min_sausage_pack * SAUSAGE_PACKAGING - total_h_d};
количество оставшихся булочек {min_bun_pack * BUN_PACKAGING - total_h_d}.
''')






Picnic_Calculator()