def ocean_level(years, level):
    year_level = 0
    print('Год\tУровень')
    print('----------------')
    for year in range(years):
        year_level += level
        print(f'{year + 1}  \t\t {year_level:.1f}')
        
        
ocean_level(25, 1.6)
