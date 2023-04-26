def get_menu_choice(L, Q):
    print()
    print('Друзья и их дни рождения')
    print('------------------------')
    print('l. Найти день рождения')
    print('2. Добавить новый день рождения')
    print('3. Изменить день рождения')
    print('4. Удалить день рождения')
    print('5. Выйти из программы')
    print()
    choice = int(input('Введите выбраный пункт: '))
    while choice < L or choice > Q: choice = int(input('Введите выбраный пункт: '))
    return choice