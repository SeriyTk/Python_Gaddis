'''
 Глобальная константа -
 это глобальное имя, ссылающееся на значение, которое нельзя изменить.
'''
CONTRIBUTION_RATE = 0.05
def main():
    show_pay_contrib(float(input('Bвeдитe заработную плату: ')))
    show_bonus_contrib(float(input('Bвeдитe сумму премий: ')))

def show_pay_contrib(gross_pay): print(f'Взнос исходя из заработной платы: ${gross_pay * CONTRIBUTION_RATE: .2f}', sep=' ')
def show_bonus_contrib(bonus): print(f'Взнос исходя из заработной платы: ${bonus * CONTRIBUTION_RATE: .2f}', sep=' ')


main()