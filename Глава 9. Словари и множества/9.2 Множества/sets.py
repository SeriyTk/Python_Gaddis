def get_name_baseball(baseball):
    print('Эти студенты состоят в бейсбольной команде: ')
    for name in baseball: print(name, end=' ')


def get_name_basketball(basketball):
    print('Эти студенты состоят в баскетбольной команде:')
    for name in basketball: print(name, end=' ')

def get_intеrsесtiоn_names(baseball,basketball):
    print('Эти студенты играют и в бейсбол, и в баскетбол:')
    for name in baseball.intersection(basketball): print(name, end=' ')

def get_union_names(baseball,basketball):
    print('Эти студенты играют в одну или обе спортивные игры:')
    for name in baseball.union(basketball): print(name, end=' ')

def get_difference_baseball(baseball,basketball):
    print('Эти студенты играют только в бейсбол:')
    for name in baseball.difference(basketball): print(name, end=' ')

def get_difference_basketball(baseball,basketball):
    print('Эти студенты играют только в бейсбол:')
    for name in basketball.difference(baseball): print(name, end=' ')

def get_symmetric_names(baseball,basketball):
    print('Эти студенты играют в одну из спортивных игр, но не в обе:')
    for name in baseball.symmetric_difference(basketball): print(name, end=' ')

