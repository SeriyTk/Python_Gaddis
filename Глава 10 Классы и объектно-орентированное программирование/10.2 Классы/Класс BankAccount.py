import bankaccount as b_a

def account_test():
    savings = b_a.BankAccount(float(input('Сколько было на счету: ')))
    savings.deposit(float(input('Вношу на счет: ')))
    print(savings)
    savings.withdraw(float(input('Сколько хотите снять со счета: ')))
    print(savings)
    

account_test()