def main():
    name_list = []
    while True:
        print('Жeлaeтe добавить имя?')
        again = input('д =да, все остальное = нет: ')
        if again != 'д': break
        else:
            name = input('Введите имя: ')
            name_list.append(name)
    print(' Вот имена, которые были введены. ')
    for name in name_list: print(name)

if __name__ == '__main__': main()