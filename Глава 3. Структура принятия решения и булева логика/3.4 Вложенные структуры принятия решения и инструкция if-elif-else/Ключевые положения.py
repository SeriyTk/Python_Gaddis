"""Для проверки более одного условия структура принятия решения может быть вложена
внутрь другой структуры принятия решения."""
def loan_qualifier():
    MIN_SALARY = 30000.0
    MIN_YEARS = 2
    salary = float(input('Годовой доход: '))
    years_on_job = int(input("Рабочий стаж: "))
    if salary >= MIN_SALARY:
        if years_on_job >= MIN_YEARS: print('Ссуда одобрена.')
        else: print("Мало стажа.")
    else: print('Мало зарабатываете.')
loan_qualifier()