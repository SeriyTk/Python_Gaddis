def main():
    '''
    with open('names.txt', 'w') as out_file:
        while True:
            name = input('Имя: ')
            if not name: break
            else: print(name, file=out_file)

    '''
    total = 0
    for name in open('names.txt'): total += 1
    print(f'Количество имен: {total}')


main()
