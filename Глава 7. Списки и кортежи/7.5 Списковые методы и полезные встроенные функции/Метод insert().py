def main():
    names = ['Джеймс', 'Кэтрин', 'Билл']
    print('Список перед вставкой:')
    for i in names: print(i, end=' ')
    names.insert(0, 'Вася')
    print()
    print('Список после вставки:')
    for i in names: print(i, end=' ')

main()