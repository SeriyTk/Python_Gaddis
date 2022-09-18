import pms

LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

FILENAME = 'employee.dat'

def main():
    employee_dct = pms.load_employee(FILENAME)
    while True:
        choice = pms.get_menu()
        if choice == QUIT: break
        else:
            if choice == LOOK_UP: pms.look_up(employee_dct)
            elif choice == ADD: pms.add(employee_dct)
            elif choice == CHANGE: pms.change(employee_dct)
            elif choice == DELETE: pms.delete(employee_dct)


    pms.save_employee(FILENAME, employee_dct)



if __name__ == '__main__': main()