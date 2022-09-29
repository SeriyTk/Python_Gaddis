import accounts as acc

def main():
    print('Введите данные о сберегательном счете.')
    acc_num = input('Номер счета: ')
    int_rate = float(input('Процентная ставка: '))
    balance = float(input('Остаток: '))

    print('Введите данные о счете CD. ')
    acc_num_cd = input('Номер счета: ')
    int_rate_cd = float(input('Процентная ставка: '))
    balance_cd = float(input('Остаток: '))
    maturity = input('Дата погашения: ')

    print(acc.Savings_Account(acc_num, int_rate, balance))
    print(acc.CD(acc_num_cd, int_rate_cd, balance_cd, maturity))


if __name__ == '__main__': main()