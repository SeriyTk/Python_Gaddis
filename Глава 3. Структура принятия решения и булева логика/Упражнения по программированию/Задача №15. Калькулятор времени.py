def Time_calculator():
    enter_seconds = int(input('Введите кол-чо секунд: '))
    days = enter_seconds // 86400
    hours = enter_seconds // 3600
    minutes = enter_seconds // 60 % 60
    print(days)
    print(hours)
    print(minutes)

Time_calculator()