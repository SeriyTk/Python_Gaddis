def Error_Collector():
    total_error = 0
    for day in range(5):
        error = int(input(f'Количество ошибок в день №{day + 1}: '))
        total_error += error

    print(f'Общее количество ошибок {total_error}')


Error_Collector()
