def get_intersection(baseball, basketball):
    for name in baseball.intersection(basketball):
        print(name)


def get_union(baseball, basketball):
    for name in baseball.union(basketball):
        print(name)

def get_play_basebal(baseball, basketball):
    for name in baseball.difference(basketball):
        print(name)

def get_play_basketball(baseball, basketball):
    for name in basketball.difference(baseball):
        print(name)

def only_one_game(baseball, basketball):
    for name in baseball.symmetric_difference(basketball):
        print(name)

def sets():
    baseball = set(['Джоди', 'Кармен', 'Аида', 'Алиция'])
    basketball = set(['Эва', 'Кармен', 'Алиция', 'Сара'])
    print('Эти студенты состоят в бейсбольной команде: ')
    for name in baseball:
        print(name)
    print()
    print('Эти студенты состоят в баскетбольной команде:')
    for name in basketball:
        print(name)
    print()
    print('Эти студенты играют и в бейсбол, и в баскетбол:')
    get_intersection(baseball, basketball)
    print()
    print('Эти студенты играют в одну или обе спортивные игры:')
    get_union(baseball, basketball)
    print()
    print('Эти студенты играют в бейсбол, но не в баскетбол:')
    get_play_basebal(baseball, basketball)
    print()
    print('Эти студенты играют в баскетбол, но не в бейсбол:')
    get_play_basketball(baseball, basketball)
    print()
    print('Эти студенты играют в одну из спортивных игр, но не в обе:')
    only_one_game(baseball, basketball)

sets()