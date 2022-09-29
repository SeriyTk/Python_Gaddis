import emplwork as e_w

def main():
    name = input('Имя сотрудника: ')
    num_empl = input('Номер сотрудника: ')
    shift_number = input("Номер смены: ")
    wage_rate = input("Ставка почасовой оплаты труда: ")
    p_w = e_w.ProductionWorker(name, num_empl, shift_number, wage_rate)
    print(p_w)

if __name__ == '__main__': main()