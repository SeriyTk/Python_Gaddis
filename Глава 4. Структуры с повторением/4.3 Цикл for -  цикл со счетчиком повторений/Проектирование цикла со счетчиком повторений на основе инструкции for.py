def speed_converter():
    INCREMENT = 10
    CONVERSION = 0.6214
    print('KPH\tMPH')
    print('------------')
    for kph in range(60, 131, 10): print(f'{kph}\t{kph * CONVERSION:.1f}')

speed_converter()