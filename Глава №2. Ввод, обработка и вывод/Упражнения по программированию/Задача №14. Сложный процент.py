def Compound_interest():
    principal_amount = float(input('Основная сумма, внесенную на сберегательный счет: '))
    annual_interest_rate = float(input('Годовая процентная ставка, начисляемая на остаток счета: '))
    accrual_frequency = float(input('Частота начисления процентного дохода в год: '))
    number_years = int(input('Количество лет: '))
    total_amount = principal_amount * (1 + annual_interest_rate / accrual_frequency) ** (accrual_frequency * number_years)


if __name__ == '__main__': Compound_interest = Compound_interest()
