import random as r


def Math_Test(num1, num2):
    print('  ', num1)
    print('+', num2)
    answer = int(input('Введите правильный ответ: '))
    if answer == num1 + num2:
        print('Ответ правильный.')
    else:
        print("Ответ не правильный.")


Math_Test(r.randint(1, 300), r.randint(1, 300))
