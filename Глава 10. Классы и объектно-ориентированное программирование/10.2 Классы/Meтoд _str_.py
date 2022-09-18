import bankaccoun1 as ba1


def main():
    saving = ba1.BankAccount(float(input('Денег на счету: ')))
    saving.deposit(float(input('Внести на счет: ')))
    print(f'Остаток на счету: ${saving.get_balance():.2f}', sep=' ')
    saving.withdraw(float(input('Сколько хотите снять? ')))
    print(saving)


if __name__ == '__main__':
    main()
