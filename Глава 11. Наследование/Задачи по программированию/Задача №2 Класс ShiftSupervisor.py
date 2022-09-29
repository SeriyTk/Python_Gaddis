import emplwork as e_w

def main():
    name = input('Имя начальника смены: ')
    num_empl = input('Номер начальника смены: ')
    number = input("Номер смены: ")
    salary = input("Оклад: ")
    bonus = input("Годовая премия: ")
    print(e_w.ShiftSupervisor(name, num_empl, number, salary, bonus))

if __name__ == '__main__': main()