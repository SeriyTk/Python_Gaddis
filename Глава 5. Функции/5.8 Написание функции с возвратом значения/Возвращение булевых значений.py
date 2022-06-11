if (int(input('Введите число: ')) % 2) ==0: print ('Это число четное. ')
else: print ('Это число нечетное.')
print()
def is_even(number) :
    if (number % 2) == 0: status = True
    else: status = False
    return status

if is_even(int(input('Введите число: '))): print ('Это число четное. ')
else: print ('Это число нечетное. ')
