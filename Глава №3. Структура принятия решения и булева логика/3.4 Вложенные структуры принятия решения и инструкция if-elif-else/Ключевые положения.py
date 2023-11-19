MIN_SALARY = 30000.0
MIN_YEARS = 2
def loan_qualifier():
    salary = float(input('Bвeдитe свой годовой доход: '))
    years_on_job = int(input('Bвeдитe количество лет рабочего стажа: '))

    if salary >= MIN_SALARY:
        if years_on_job >= MIN_YEARS: print('Ваша ссуда одобрена.')
        else: print(f'Bы должны отработать не менее {MIN_YEARS} лет, чтобы получить одобрение.')
    else: print(f'Bы должны зарабатывать не менее $ {MIN_SALARY:,.2f} в год, чтобы получить одобрение.')


if __name__ == '__main__': loan_qualifier = loan_qualifier()
