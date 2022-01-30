import random as r


def Math_Test(num1, num2):
    print('  ',num1)
    print('+', num2)
    print(num1 + num2)


Math_Test(r.randint(1, 300), r.randint(1, 300))
