def table_correspondence():
    print('Цельсий\tФаренгейт')
    print('------------------------')
    for i in range(21):
        F = 9 / 5 * i + 32
        print(f'{i}       \t       {F:.1f}')


table_correspondence()
