'''
Цикл со счетчиком повторений повторяется заданное количество раз.
В Python для написания цикла со счетчиком повторений применяется инструкция for.

for переменная in [значениеl, значение2, ... ] :
    инструкция
    инструкция
    ...
'''
def simple_loop1():
    lst = [1, 2, 3, 4, 5]
    for i in lst:
        print(i, end=' ')


simple_loop1()
print()
def simple_loop2():
    lst = [1, 3, 5, 7, 9]
    for i in lst:
        print(i, end=' ')


simple_loop2()
print()
def simple_loopЗ():
    list = [ 'Мигнуть ' , 'Моргнуть', 'Кивнуть']
    for i in list:
        print(i, end=' ')


simple_loopЗ()