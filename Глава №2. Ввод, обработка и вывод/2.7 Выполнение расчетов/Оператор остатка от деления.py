
def time_converter():
    total_seconds = float(input('Bвeдитe количество секунд: '))
    print('Boт время в часах, минутах и секундах :')
    print(f'''
Часы: {total_seconds // 3600}
Минуты: {(total_seconds // 60) % 60}
Секунды: {total_seconds % 60}
''')

if __name__ == '__main__': time_converter()