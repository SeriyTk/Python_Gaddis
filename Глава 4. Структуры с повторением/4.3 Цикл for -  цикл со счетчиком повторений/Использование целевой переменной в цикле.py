def squares():
    print('Число\tКвадрат числа')
    print('---------------------------')
    for num in range(1, 11): square = num ** 2; print(f'{num}      \t            {square}')

squares()