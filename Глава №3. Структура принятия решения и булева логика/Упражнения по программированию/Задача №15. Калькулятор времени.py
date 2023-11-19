def Time_calculator():
    total_seconds = int(input('Bвeдитe количество секунд: '))
    print('Boт время в днях, часах, минутах и секундах :')
    if total_seconds < 60: print(f'''
Дни: {int(total_seconds // 3600 // 24):d}
Часы: {int(total_seconds // 3600):d}
Минуты: {int((total_seconds // 60) % 60):d}
Секунды: {int(total_seconds % 60):d}
''')
    elif 60<= total_seconds < 3600: print(f'''
Дни: {int(total_seconds // 3600 // 24):d}
Часы: {int(total_seconds // 3600):d}
Минуты: {int((total_seconds // 60) % 60):d}
Секунды: {int(total_seconds % 60):d}
''')
    elif 3600 <= total_seconds < 86400: print(f'''
Дни: {int(total_seconds // 3600 // 24):d}
Часы: {int(total_seconds // 3600):d}
Минуты: {int((total_seconds // 60) % 60):d}
Секунды: {int(total_seconds % 60):d}
''')
    elif total_seconds >= 86400: print(f'''
Дни: {int(total_seconds // 3600 // 24):d}
Часы: {int(total_seconds // 3600 % 24):d}
Минуты: {int((total_seconds // 60) % 60):d}
Секунды: {int(total_seconds % 60):d}
''')



if __name__ == '__main__': Time_calculator = Time_calculator()
