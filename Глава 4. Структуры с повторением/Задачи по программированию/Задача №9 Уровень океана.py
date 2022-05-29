LEVEL = 1.6


def ocean_level():
    print('Год\tУровень')
    for year in range(25): print(f'{year + 1}   \t     {(year + 1) * LEVEL:.1f}')


ocean_level()
