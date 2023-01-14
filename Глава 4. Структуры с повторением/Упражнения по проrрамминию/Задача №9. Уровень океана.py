def ocean_level():
    LEVEL = 1.6
    YEARS = 25
    total_level = 0
    print('Год\tУровень')
    print('----------------')
    for year in range(YEARS): total_level += LEVEL; print(f'{year +1}   \t\t    {total_level:.1f}')
ocean_level()