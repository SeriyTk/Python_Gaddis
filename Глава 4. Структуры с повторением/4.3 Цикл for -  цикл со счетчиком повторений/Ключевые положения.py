'''Цикл со счетчиком повторений повторяется заданное количество раз.
В Python для написания цикла со счетчиком повторений применяется инструкция for.

for переменная in [значениеl, значение2, ... ] :
    инструкция
    инструкция
    . . .
'''
def simple_loop1():
    print('Я покажу числа от 1 до 5. ')
    for num in [1, 2, 3, 4, 5]: print(num)

simple_loop1()

def simple_loop2():
    print('Я покажу числа от 1 до 9. ')
    for num in [1, 3, 5, 7, 9]: print(num)

simple_loop2()

def simple_loop3():
    for name in ['Мигнуть',  'Моргнуть ', 'Кивнуть']: print(name)

simple_loop3()