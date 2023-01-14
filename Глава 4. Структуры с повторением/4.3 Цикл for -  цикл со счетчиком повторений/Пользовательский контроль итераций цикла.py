def user_squares1():
    print('Эта программа выв оди т список чисел (начиная с 1) и их квадраты.')
    end = int(input('Насколько много: '))
    print()
    print('Число \tКвадрат числа')
    print('----------------------------')
    for num in range(1, end +1): squear = num ** 2; print(f'{num}\t{squear}')

user_squares1()
print()
def user_squares2():
    print('Эта программа выв оди т список чисел (начиная с 1) и их квадраты.')
    start = int(input('Начальное число: '))
    end = int(input('Насколько много: '))
    print()
    print('Число \tКвадрат числа')
    print('----------------------------')
    for num in range(1, end + 1): squear = num ** 2; print(f'{num}\t{squear}')

user_squares2()