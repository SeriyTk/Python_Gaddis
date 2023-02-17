'''Исключение -
 это ошибка, которая происходит во время работы программы, приводящая к ее внезапному останову.
Для корректной обработки исключений используется инструкция try/except.'''
def division():
    num1 = int(input('Введите число: '))
    num2 = int(input('Введите еще число: '))
    result = num1 / num2
    print(f'{num1} деленное на {num2} равно {result}')
def division2():
    num1 = int(input('Введите число: '))
    num2 = int(input('Введите еще число: '))
    if num2 != 0: result = num1 / num2; print(f'{num1} деленное на {num2} равно {result}')
    else: print('Деление на ноль невозможно.')

    if __name__ == '__main__': division2()
print()
def gross_pay1():
    hours = int(input('Сколько часов вы отработали? '))
    pay_rate = float(input('Bвeдитe свою почасовую ставку :'))
    gross_pay = hours * pay_rate
    рrint(f'Заработная плата: ${gross_pay:,.2f}')

    if __name__ == '__main__': gross_pay1()
'''
try :
    инструкция
    инструкция
    . . .
except ИмяИсключения:
    инструкция
    инструкция
    . . .
'''
def gross_pay2():
    try:
        hours = int(input('Сколько часов вы отработали? '))
        pay_rate = float(input('Bвeдитe свою почасовую ставку :'))
        gross_pay = hours * pay_rate
        рrint(f'Заработная плата: ${gross_pay:,.2f}')
    except ValueError: print ('ОШИБКА: Отработанные часы и почасовая ставка оплаты должны быть допустимыми числами.')

    if __name__ == '__main__': gross_pay2()
def display_file():
    filename = input('Введите имя файла: ')
    try:
        with open(filename) as infile:
            contents = infile.read()
            print(contents)
    except IOError: print ('Произошла ошибка при попытке прочитать фaйл', filename)

if __name__ == '__main__': display_file()
