def WiFi_check():
    while True:
        print('WI-FI работат?')
        enter = input('Если да нажмите 1, если нет enter: ')
        if enter == '1': print('Пользуйтесь.'); break
        else:
            print('Перезагрузите компьютер и попробуйте подключиться.')
            print('Вы исправили проблему?')
            enter = input('Если да нажмите 1, если нет enter: ')
            if enter == '1': print('Пользуйтесь.'); break
            else:
                print('Перезагрузите маршрутизатор и попробуйте подключиться.')
                print('Вы исправили проблему?')
                enter = input('Если да нажмите 1, если нет enter: ')
                if enter == '1': print('Пользуйтесь.'); break
                else:
                    print('Убедитесь, что кабели между маршрутизатором и модемом прочно подсоединены.')
                    print('Вы исправили проблему?')
                    enter = input('Если да нажмите 1, если нет enter: ')
                    if enter == '1': print('Пользуйтесь.'); break
                    else:
                        print('Переместите маршрутизатор на новое место.')
                        print('Вы исправили проблему?')
                        enter = input('Если да нажмите 1, если нет enter: ')
                        if enter == '1': print('Пользуйтесь.'); break
                        else: print('Возьмите новый маршрутизатор.'); break



WiFi_check()