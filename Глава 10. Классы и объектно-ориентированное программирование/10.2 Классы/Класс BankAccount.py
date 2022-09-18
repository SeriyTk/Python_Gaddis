import bankaccoun as ba

def main():
    saving = ba.BankAccount(float(input('Денег на счету: ')))
    saving.deposit(float(input('Внести на счет: ')))
    print(f'Остаток на счету: ${saving.get_balance():.2f}', sep=' ')
    saving.withdraw(float(input('Сколько хотите снять? ')))
    print(f'Остаток на счету: ${saving.get_balance():.2f}', sep=' ')
if __name__ == '__main__':
    main()