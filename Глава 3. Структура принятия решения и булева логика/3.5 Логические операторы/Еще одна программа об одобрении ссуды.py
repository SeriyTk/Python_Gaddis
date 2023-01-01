def loan_qualifier():
    MIN_SALARY = 30000.0
    MIN_YEARS = 2
    salary = float(input('Годовой доход: '))
    years_on_job = int(input("Рабочий стаж: "))
    if salary >= MIN_SALARY or years_on_job >= MIN_YEARS: print('Ссуда одобрена.')
    else: print("Ссуда не одобрена.")

loan_qualifier()