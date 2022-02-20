def Name_search():
    with open(r'G:\GirlNames.txt') as f_GN, open(r'G:\BoyNames.txt') as f_BN:
        list_girls = []
        list_boys = []
        for g_n in f_GN:
            list_girls.append(g_n.rstrip())
        print(list_girls)
        for b_n in f_BN:
            list_boys.append(b_n.rstrip())
        print(list_boys)
    name_girl = input('Введите имя девочки: ')
    if name_girl in list_girls:
        print(f'{name_girl} находится среди популярных.')
    name_boy = input('Введите имя мальчика: ')
    if name_boy in list_boys:
        print(f'{name_boy} находится среди популярных.')

Name_search()