def none_demo():
    num1 = int(input('Bвeдитe число: '))
    num2 = int(input('Bвeдитe еще одно число: '))
    quotient = divide(num1, num2)

    if quotient is None: print('Деление на ноль невозможно.' )
    else: print(f'{num1} поделить на {num2} равняется {quotient}. ')

def divide(num1, num2):
    if num2 == 0: result = None
    else: result = num1 / num2
    return result

if __name__ == '__main__': none_demo()