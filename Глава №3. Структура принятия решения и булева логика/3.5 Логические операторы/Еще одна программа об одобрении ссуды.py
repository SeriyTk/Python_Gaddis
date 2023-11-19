MIN_SALARY = 30000.0
MIN_YEARS = 2
def loan_qualifier3():
    salary = float(input('Bвeдитe свой годовой доход: '))
    years_on_job = int(input('Bвeдитe количество лет рабочего стажа: '))
    if salary >= MIN_SALARY or years_on_job >= MIN_YEARS: print('Baшa ссуда одобрена.')
    else: print('Ваша ссуда не одобрена.')


if __name__ == '__main__': loan_qualifier3 = loan_qualifier3()
