def retirement(CONTRIBUTION_RATE):
    gross_pay = float(input('Введите заработную плату: '))
    bonus = float(input('Сумма премий: '))
    pay_contrib = show_pay_contrib(gross_pay, CONTRIBUTION_RATE)
    bonus_contrib = show_bonus_contrib(bonus, CONTRIBUTION_RATE)
    print(f'Взнос исходя из заработной платы {pay_contrib:,.2f}.', sep=' ')
    print(f'Взнос исходя из премий {bonus_contrib:,.2f}.', sep=' ')


def show_pay_contrib(gross_pay, CONTRIBUTION_RATE):
    return gross_pay * CONTRIBUTION_RATE


def show_bonus_contrib(bonus, CONTRIBUTION_RATE):
    return bonus * CONTRIBUTION_RATE


retirement(0.05)
