LEVEL = 1.6
YEARS = 25
def Ocean_level():
    level = 0
    print('Год  \t \t Уровень')
    for year in range(YEARS): level += LEVEL; print(f'{year + 1}   \t \t {level:.1f}')


if __name__ == '__main__': Ocean_level = Ocean_level()
