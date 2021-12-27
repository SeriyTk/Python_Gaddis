# Для проверки более одного условия структура принятия решения может быть вложена
# внутрь другой структуры принятия решения.
def loan_qualifier():
    MIN_SALARY = 30000
    MIN_YEARS = 2
    salary = float(input('Ваша зарплата за год: '))
    if salary < MIN_SALARY:
        print('Иди отсюда голодранец.')
    else:
        year_job = int(input('Ваш стаж работы: '))
        if year_job < MIN_YEARS:
            print('Маловато работаете. Прийдите через годик-два.')
        else:
            print('Заходи дорогой! Получай кредит.')

loan_qualifier()
