import birthdays as b_s

def main():
    birthdays = {}
    b_s.display_menu()
    while True:
        choice = int(input('Выберите пункт меню: '))
        if 1 > choice or choice > 5: print('Такого пункта меню нет.')
        else:
            if choice == 5: print('Программа завершена.'); break
            elif choice == 1: b_s.add(birthdays)
            elif choice == 2: b_s.look_up(birthdays)
            elif choice == 3: b_s.change(birthdays)
            elif choice == 4: b_s.delete(birthdays)

main()