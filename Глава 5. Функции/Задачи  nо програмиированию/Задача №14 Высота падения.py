def main():
    falling_dtstance(int(input('Время падения тела: ')))


def falling_dtstance(t):
    print('Секунды\tМетры')
    for i in range(t):
        print(f'{i + 1}   \t\t     {1 / 2 * 9.8 * (i + 1) ** 2:.1f}')


main()
