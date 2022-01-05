def Time_calculator():
    number_of_seconds = int(input('Количество секунд: '))
    day = number_of_seconds // 86400
    hour = (number_of_seconds // 3600) % 24
    minute = (number_of_seconds // 60) % 60
    second = number_of_seconds % 60
    print('Дни\t Часы\t Минуты\t Секунды')
    print(f' {day} \t:\t {hour} \t:\t {minute} \t:\t {second}')


Time_calculator()
