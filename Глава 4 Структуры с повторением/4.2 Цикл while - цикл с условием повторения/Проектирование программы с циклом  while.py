def temperature():
    NORMAL = 102.5
    substance_temperature = float(input("Введите температуру вещества: "))
    while substance_temperature > NORMAL:
        print('Убавьте нагрев, подождите 5 минут и проверьте температуру снова.')
        substance_temperature = float(input("Введите температуру вещества: "))
    else:
        print("Температура в норме. Проверить температуру через 15 минут.")


temperature()
