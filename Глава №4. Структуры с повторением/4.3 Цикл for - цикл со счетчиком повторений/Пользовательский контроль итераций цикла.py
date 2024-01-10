def user_squares1():
    print('Эта программа выводит список чисел (начиная с 1) и их квадраты.')
    end = int(input('Hacкoлькo далеко мне заходить? '))
    print()
    print('Число \t Квадрат числа')
    print('----------------------------')
    for num in range(1, end + 1): square = num ** 2; print(f'{num}             \t{square}')



    if __name__ == '__main__': user_squares1 = user_squares1()

def user_squares2():
    print('Эта программа выводит список чисел (начиная с 1) и их квадраты.')
    start = int(input(' Bвeдитe начальное число: ') )
    end = int(input('Hacкoлькo далеко мне заходить? '))
    print()
    print('Число \t Квадрат числа')
    print('----------------------------')
    for num in range(start, end + 1): square = num ** 2; print(f'{num}              \t     {square}')



if __name__ == '__main__': user_squares2 = user_squares2()
