def speed_converter():
    START = 60
    END = 130
    STEP = 10
    print(f'Км\час\tМиль\час')
    for i in range(START, END + 1, STEP):
        mph = i * 0.6214
        print(f'{i} \t  \t{mph:.1f}')


speed_converter()
