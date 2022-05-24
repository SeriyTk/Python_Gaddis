'''
Для проверки более одного условия структура принятия решения может быть вложена
внутрь другой структуры принятия решения.
'''
MIN_SALARI = 30000.0
MIN_YEARS = 2

def loan_qualifier():
    salary = float(input('Ваш годовой оклад: '))
    years_of_job = int(input('Количество отработанных лет: '))
    if salary >= MIN_SALARI:
        if years_of_job >= MIN_YEARS:
            print('Ссуда одобрена.')
        else:
            print(f'Вы дожны отработать не менее {MIN_YEARS} лет')
    else:
        print(f'Вы дожны зарабатывать не менее {MIN_SALARI:,.2f}', sep=' ')


loan_qualifier()