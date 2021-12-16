def time_converter():
    total_seconds = int(input('Получить количество секунд: '))
    hours = total_seconds // 3600
    minutes = (total_seconds // 60) % 60
    seconds = total_seconds % 60
    print(f'Часы: {hours}, минуты: {minutes}, секунды: {seconds}.')


time_converter()
