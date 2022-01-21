def population(start, increase, days):
    total = 0
    print('День\tПопуляция')
    print('---------------------')
    for day in range(days):
        res = start + (total * increase)
        total += res
        print(f'{day + 1}  \t\t  {res}')


population(2, 0.3, 10)
