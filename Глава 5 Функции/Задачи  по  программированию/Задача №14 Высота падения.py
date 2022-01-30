def Drop_Height(times):
    print('Время \t Расстояние')
    for time in range(1, times + 1):
        dist = 1 / 2 * 9.8 * time ** 2
        print(f'{time}   \t\t {dist:.1f}')
        
        
Drop_Height(10)
