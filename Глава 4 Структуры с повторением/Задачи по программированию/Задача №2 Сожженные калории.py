def Calories_burned(start, stop, step):
    print('Минуты\tКалории')
    for minutes in range(start, stop + 1, step):
        cal_min = 4.2
        calories = minutes * cal_min
        print(f'{minutes}  \t \t    {calories}')


Calories_burned(10, 30, 5)
