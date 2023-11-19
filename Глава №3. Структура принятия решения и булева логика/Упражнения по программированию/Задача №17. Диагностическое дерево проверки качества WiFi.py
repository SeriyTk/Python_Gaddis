def WiFi_quality_checks():
    print('Перезагрузите компьютер и попробуйте подключиться.')
    request = input('Вы исправили проблему? ')
    if request == "нет": print("Перезагрузите маршрутизатор и попробуйте подключиться."); request = input('Вы исправили проблему? ')
    if request == "нет": print("Убедитесь, что кабели между маршрутизатором и модемом прочно подсоединены."); request = input('Вы исправили проблему? ')
    if request == "нет": print("Переместите маршрутизатор на новое место."); request = input('Вы исправили проблему? ')
    if request == "нет": print('Возьмите новый маршрутизатор.')
    if request == "да": print('На здоровье.')



if __name__ == '__main__': WiFi_quality_checks = WiFi_quality_checks()
