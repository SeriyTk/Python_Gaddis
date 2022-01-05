# Цикл с условием повторения исполняет инструкции или набор инструкций повторно
# до тех пор, пока условие является истинным. В  Python  для написания цикла с условием
# повторения применяется инструкция  while.
# while условие:
#   инструкция
#   инструкция
def commission():
    keep_going = 'д'
    while keep_going == 'д':
        sales = float(input('Объем продаж: '))
        comm_rate = float(input('Комиссионные: '))
        commission = sales * comm_rate
        print(f'Комиссионые составляют ${commission:,.2f}.')

        keep_going = input('Если хотите продолжить введите "д": ')

    print('Программа завершена.')

commission()

