import empl_prod as e_p
DAY = 1
NIGHT = 2
def main():
    name = input('Имя рабочего: ')
    id = input('Номер: ')
    while True:
        shift_num = int(input("Номер смены: "))
        if shift_num != DAY and shift_num != NIGHT: print('Таких смен нет.')
        else:
            rate = float(input('Почасовая оплата: '))
            annual_salary = float(input('Годовой оклад: '))
            annual_bonus = float(input('Годовая премия: '))
            shiftsupervisor = e_p.ShiftSupervisor(name, id, shift_num, rate, annual_salary, annual_bonus)
            break
    print(f'''
Имя рабочего: {shiftsupervisor.get_name()}
номер рабочего: {shiftsupervisor.get_id()}
номер смены: {shiftsupervisor.get_shift_num()}
ставка почасовой оплаты труда: {shiftsupervisor.get_rate():,.2f}
годовой оклад: {shiftsupervisor.get_annual_salary():,.2f}
годовая премия: {shiftsupervisor.set_annual_bonus():,.2f}
''')

if __name__ == '__main__': main()
