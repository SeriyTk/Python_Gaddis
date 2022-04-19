import bankaccount as b_a


def account_test():
    savings = b_a.BankAccount(float(input('Сколько было на счету: ')))
    savings.deposit(float(input('Вношу на счет: ')))
    #print(f'Сейчас на вашем счету {savings.get_balance():.2f}')
    print(savings)
    savings.withdraw(float(input('Сколько хотите снять со счета: ')))
    #print(f'Сейчас на вашем счету {savings.get_balance():.2f}')
    print(savings)


account_test()
