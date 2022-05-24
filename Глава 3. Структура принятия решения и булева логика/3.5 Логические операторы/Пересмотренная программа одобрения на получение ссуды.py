MIN_SALARY = 30000.0
MIN_YEARS = 2

def loan_qualifier():
    salary = int(input('Годовой оклад: '))
    years_on_job = int(input('Рабочий стаж: '))
    if salary >= MIN_SALARY and years_on_job >= MIN_YEARS: print ('Ваша ссуда одобрена.')
    else: print ('Ваша ссуда не одобрена.')

loan_qualifier()