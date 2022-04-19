import modules as mod
FILENAME = 'pms.dat'

def Personnel_management_system():
    pers_man_sys = mod.load_empt(FILENAME)
    while True:
        chois = mod.chois_menu()

        if  chois == 5:
            print('Программа завершена.')
            break
        else:
            if chois == 1:
                mod.look_up(pers_man_sys)
            elif chois == 2:
                mod.add(pers_man_sys)
            elif chois == 3:
                modt.change(pers_man_sys)
            elif chois == 4:
                mod.delete(pers_man_sys)

    mod.save_empt(FILENAME, pers_man_sys)

Personnel_management_system()

