def main():
    list_charge_acc = [acc.rstrip() for acc in open('G:\charge_accounts.txt')]
    print(list_charge_acc)
    if input('Введите номер: ') in list_charge_acc: print('Номер допустимый.')
    else: print("Номер не допустимый.")



main()
