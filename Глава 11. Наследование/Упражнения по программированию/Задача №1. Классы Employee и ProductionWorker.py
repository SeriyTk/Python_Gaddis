import empl_prod as e_p
DAY = 1
NIGHT = 2
def main():
    name = input('Имя рабочего: ')
    id = input('Номер: ')
    while True:
        shift_num = int(input("Номер смены: "))
        if shift_num != DAY and shift_num != NIGHT:
            print('Таких смен нет.')
        else:
            rate = float(input('Почасовая оплата: '))
            employee = e_p.ProductionWorke(name, id, shift_num, rate)
            break
    print(f'''
Имя рабочего: {employee.get_name()}
номер рабочего: {employee.get_id()}
номер смены: {employee.get_shift_num()}
ставка почасовой оплаты труда: {employee.get_rate():,.2f}
''')



if __name__ == '__main__': main()
