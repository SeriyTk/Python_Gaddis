import contact


LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

FILENAME = 'contacts.dat'

def main():
    mycontacts = contact.load_file(FILENAME)
    choice = 0
    while choice != QUIT:
        choice = contact.get_menu()
        if choice == LOOK_UP: contact.look_up(mycontacts)
        elif choice ==ADD: contact.add(mycontacts)
        elif choice == CHANGE: contact.change(mycontacts)
        elif choice == DELETE: contact.delete(mycontacts)

    contact.save_contacts(FILENAME, mycontacts)




if __name__ == '__main__': main()