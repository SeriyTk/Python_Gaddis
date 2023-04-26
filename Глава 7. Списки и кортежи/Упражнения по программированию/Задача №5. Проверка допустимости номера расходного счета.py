def main():
    with open('charge_accounts.txt') as infile:
        list_accounts = [int(num) for num in infile]
        if int(input("Номер счета: ")) in list_accounts: print('Да')
        else: print("Нет")

if __name__ == '__main__': main()