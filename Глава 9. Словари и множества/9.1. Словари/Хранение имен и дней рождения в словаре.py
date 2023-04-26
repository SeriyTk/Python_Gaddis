import menu_choice as m_ch, look_up as l_up, add, change as ch, delete as delt
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5
def main():
    birthdays = {}
    choice = 0
    while choice != QUIT:
        choice = m_ch.get_menu_choice(LOOK_UP, QUIT)
        if choice == LOOK_UP: l_up.look_up(birthdays)
        elif choice == ADD: add.add(birthdays)
        elif choice == CHANGE: ch.change(birthdays)
        elif choice == DELETE: delt.delete(birthdays)


if __name__ == '__main__': main()