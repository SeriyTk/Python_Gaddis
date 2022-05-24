def Days_in_February():
    year = int(input('Год: '))
    if (year % 100 == 0 and year % 400 == 0 or
            year % 100 != 0 and year % 4 == 0): print(f'Год {year} высокосный.')
    else: print(f'Год {year} не высокосный.')


Days_in_February()