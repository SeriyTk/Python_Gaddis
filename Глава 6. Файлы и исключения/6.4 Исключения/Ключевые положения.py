def main():
    num1 = int(input('Введите число: '))
    num2 = int(input('Bвeдитe еще одно число: '))
    if num2 != 0: print(f'{num1} деленное на {num2} равняется {num1 / num2}')
    else: print ('Нельзя делить на ноль.')

def main():
    try:
        gross_pay = int(input('Cкoлькo часов вы отработали? ')) * float(input('Bвeдитe свою почасовую ставку: '))
        print(f'Зарплата: ${gross_pay:.2f}',sep='')
    except ValueError: print('Ошибка! Нужно вводить числа.')


def main():
    try:
        with open(input ('Введите имя файла: ')) as infile:
            print(infile.read())
    except FileNotFoundError: print('Такого файла нет.')

main()