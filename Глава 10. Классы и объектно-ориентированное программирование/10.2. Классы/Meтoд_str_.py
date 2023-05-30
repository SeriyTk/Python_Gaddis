import bankaccount2 as b_a
def main():
    start_bal = float(input('Bвeдитe свой начальньм остаток: '))
    savings = b_a.BankAccount(start_bal)
    pay = float(input('Сколько Вы получили на этой неделе? '))
    print('Вношу эту сумму на Ваш счет.')
    savings.deposit(pay)
    print(f'Baш остаток на счете составляет ${savings.get_balance():,.2f}.')

    cash = float(input('Kaкyю сумму Вы желаете снять со счета? '))
    print('Снимаю эту сумму с Вашего банковского счета.')
    savings.withdraw(cash)
    print(savings)

if __name__ == '__main__': main()
