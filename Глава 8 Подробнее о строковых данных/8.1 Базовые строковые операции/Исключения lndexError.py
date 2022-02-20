my_string = 'Ромашки белые'
try:
    print(my_string[20])
except IndexError:
    print('Индекс отсутствует.')
