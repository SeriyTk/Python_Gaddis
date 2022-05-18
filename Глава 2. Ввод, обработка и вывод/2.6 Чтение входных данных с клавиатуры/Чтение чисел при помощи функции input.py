string_value = input('Сколько часов Вы отработали? ')
hours = int(string_value)
print(hours)
hours1 = int(input('Сколько часов Вы отработали? '))
print(hours1)
pay_rate = float(input('Kaкaя у вас почасовая ставка оплаты труда? '))
print(pay_rate)

def inpt():
    name = input('Как Вас зовут?  ' )
    age = int(input('Cкoлькo Вам лет? '))
    income = float(input('Kaкoй у Вас доход? '))
    print('Вот данные, которые Вы ввели:')
    print(f'''
Имя: {name}
Возвраст: {age}
Доход: {income}
''')

inpt()