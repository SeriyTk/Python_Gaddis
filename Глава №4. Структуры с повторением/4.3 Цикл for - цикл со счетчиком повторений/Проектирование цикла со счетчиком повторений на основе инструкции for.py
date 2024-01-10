START_SPEED = 60
END_SPEED = 131
INCREMENT = 10
CONVERSION_FACTOR = 0.6214
def speed_converter():
    print('KPH     MPH')
    print('-------------- ')
    for kph in range(START_SPEED, END_SPEED, INCREMENT): mph = kph * CONVERSION_FACTOR; print ( f'{kph}    \t {mph:.1f} ')


if __name__ == '__main__': speed_converter = speed_converter()
