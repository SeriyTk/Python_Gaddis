def time_converter():
    total_second = float(input('Количество секунд: '))

    hours = total_second // 3600
    minutes = (total_second // 60) % 60
    seconds = total_second % 60

    print(f'''Вот время в часах, минутах, секундах:
    Часы: {hours}
    Минуты: {minutes}
    Секунды: {seconds}
''')


time_converter()