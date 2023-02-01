CONTRIBUTION_RATE = 0.05
def retirement():
    gross_pay = float(input('Bвeдитe заработную плату: '))
    bonus = float(input('Bвeдитe сумму премий: '))
    show_pay_contrib(gross_pay)
    show_bonus_contrib(bonus)

def show_pay_contrib(gross): print (f'Взнос исходя из заработной платы: ${gross * CONTRIBUTION_RATE:,.2f}.')
def show_bonus_contrib(bonus): print(f'Bзнoc исходя из суммы премий: ${bonus * CONTRIBUTION_RATE:,.2f}.')
if __name__ == '__main__': retirement()