def Calories_burned():
    CALOR_MIN = 4.2
    START = 10
    END = 30
    STEP = 5
    print('Время\tКалории')
    print('--------------------')
    for time in range(START, END + STEP, STEP): print(f'{time}\t\t {time * CALOR_MIN}')

Calories_burned()