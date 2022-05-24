def Time_calculator():
    total_seconds = int(input('Количество секунд: '))
    if 60 <= total_seconds < 3600: print(f'Минуты: {total_seconds // 60}, секунды: {total_seconds % 60}')
    elif 3600 <= total_seconds < 86400 : print(f'Часы: {total_seconds // 3600}, минуты: {(total_seconds // 60) % 60}, секунды: {total_seconds % 60}')
    elif 86400 <= total_seconds: print(f'Дни: {total_seconds // 86400}, часы: {(total_seconds // 3600) % 24}, минуты: {(total_seconds // 60) % 60}, секунды: {total_seconds % 60}')


Time_calculator()
