START_SPEED = 60
END_SPEED = 131
INCREMENT = 10
CONVERSION = 0.6214

def speed_converter():
    print("Км.ч \t  Миль.ч")
    print('-------------------')
    for kph in range(START_SPEED, END_SPEED, INCREMENT): mph = kph *CONVERSION; print(f' {kph}   \t   {mph:.1f}')

speed_converter()