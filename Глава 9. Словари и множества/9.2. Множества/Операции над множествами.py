def main():
    baseball = set(['Джоди', 'Кармен', 'Аида', 'Алисия'])
    basketball = set(['Eвa', 'Кармен', 'Алисия', 'Сара'])
    print('Эти студенты состоят в бейсбольной команде: ')
    for name in baseball: print(name)
    print()
    print('Эти студенты состоят в баскетбольной команде: ')
    for name in basketball: print(name)
    print()
    print(' Эти студенты играют и в бейсбол, и в баскетбол: ')
    for name in baseball.intersection(basketball): print(name)
    print()
    print('Эти студенты играют в одну или обе спортивные игры: ')
    for name in baseball.union(basketball): print(name)
    print()
    print('Эти студенты играют в бейсбол, но не в баскетбол: ')
    for name in baseball.difference(basketball): print(name)
    print()
    print('Эти студенты играют в баскетбол, но не в бейсбол: ')
    for name in basketball.difference(baseball): print(name)
    print()
    print('Эти студенты играют в одну из спортивных игр, но не в обе: ')
    for name in baseball.symmetric_difference(basketball): print(name)


if __name__ == '__main__': main()