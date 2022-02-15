def insert_list():
    names = ['Джеймс', 'Кэтрин', 'Билл']
    print('Список перед вставкой:')
    print(names)
    names.insert(0, input('Какое имя вставить: '))
    print('Список после вставки:')
    print(names)

insert_list()
