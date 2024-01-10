DAYS = 5
def Error_Collector():
    total_error = 0
    for day in range(DAYS):
        error = int(input(f'Количество ошибок в {day + 1} день: '))
        total_error += error

    print()
    print(f'Общее количество ошибок - {total_error}.')


if __name__ == '__main__': Error_Collector = Error_Collector()
