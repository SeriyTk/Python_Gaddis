def is_even(number):
    if (number % 2) == 0: status = True
    else: status = False
    return status
number = int(input('Число: '))
if is_even(number): print('Это число четное.')
else: print('Этo число нечетное.')