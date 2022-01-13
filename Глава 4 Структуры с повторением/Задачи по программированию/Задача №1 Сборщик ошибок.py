def Bug_collector(n):
    total_bugs = 0
    for day in range(n):
        bugs_day = int(input(f'Количество ошибок в течении дня №{day + 1}: '))
        total_bugs += bugs_day

    return total_bugs


days = int(input('Количество дней: '))
print(Bug_collector(days))
