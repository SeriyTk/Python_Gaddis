number = 22
print(f'Чиcлo равняется {number:10}')
print()
name = 'Джей'
print(f'Пpивeт {name:10}.Рад познакомиться.')
print()
def center_align():
    name1 = 'Гордон'
    name2 = 'Смит'
    name3 = 'Вашингтон'
    name4 = 'Альварадо'
    name5 = 'Ливингстон'
    name6 = 'Джонс'

    print(f'***{name1:^20}***')
    print(f'***{name2:^20}***')
    print(f'***{name3:^20}***')
    print(f'***{name4:^20}***')
    print(f'***{name5:^20}***')
    print(f'***{name6:^20}***')

if __name__ == '__main__': center_align()
