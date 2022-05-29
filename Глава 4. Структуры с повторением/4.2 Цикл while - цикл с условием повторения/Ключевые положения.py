"""
Цикл с условием повторения исполняет инструкции или набор инструкций повторно
до тех пор, пока условие является истинным. В Python для написания цикла с условием
повторения применяется инструкция while.

while условие:
    инструкция
    инструкция
"""
def commission():
    keep_going = 'д'
    while keep_going == 'д':
        sales = float(input('Введите объем продаж: '))
        comm_rate = float(input('Ставка комиссионных: '))
        commission = sales * comm_rate

        print(f'Комиссионное вознаграждение составляет ${commission:,.2f}',sep=' ')

        keep_going = input('Хотите вычислить еще одно? Введите д, если да: ')


x = 'spam'
while x:
    print(x, end=' ')
    x = x[1:]
print()
a = 0; b = 10
while a < b: print(a, end=' '); a += 1