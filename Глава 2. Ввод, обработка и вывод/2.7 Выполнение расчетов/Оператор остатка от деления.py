def time_converter():
    total_second = int(input('Количество секунд: '))

    hours = total_second // 3600
    minutes = (total_second // 60) % 60
    seconds = total_second % 60

    print('Boт время в часах, минутах и секундах: ')
    print("Часы: ",hours)
    print("Минуты: ",minutes)
    print("Секунды: ",seconds)

time_converter()