import contact
FILENAME = 'contacts.dat'


def contact_manager():
    mycontacts = contact.load_contacts(FILENAME)
    while True:
        chois = contact.chois_menu()

        if  chois == 5:
            print('Программа завершена.')
            break
        else:
            if chois == 1:
                contact.look_up(mycontacts)
            elif chois == 2:
                contact.add(mycontacts)
            elif chois == 3:
                contact.change(mycontacts)
            elif chois == 4:
                contact.delete(mycontacts)


    contact.save_contacts(FILENAME,mycontacts)



contact_manager()

