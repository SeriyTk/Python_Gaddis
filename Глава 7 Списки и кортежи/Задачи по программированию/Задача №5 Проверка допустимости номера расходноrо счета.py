def Validation():
    search_acc = input('Введите номер аккаунта: ')
    with open(r'G:\charge_accounts.txt') as f_acc:
        list_acc = []
        line = f_acc.readline()
        while line != '':
            list_acc.append(line.rstrip())
            line = f_acc.readline()
        if search_acc in list_acc:
            print(f'Номер {search_acc} допустимый.')
        else:
            print(f'Номер {search_acc} не допустимый.')




Validation()
