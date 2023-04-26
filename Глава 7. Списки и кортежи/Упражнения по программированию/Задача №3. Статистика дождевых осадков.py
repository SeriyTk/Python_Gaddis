MONTHS = 12
def main():
    list_months = []
    for month in range(MONTHS):
        precipitation = int(input(f'Количество осадков в месяце №{month + 1}: '))
        list_months.append(precipitation)

    total = get_total(list_months)
    average = get_average(total, list_months)
    print(f'''
Общее количество осадков за год: {total} ;
среднее количество осадков за месяц: {average}
{max(list_months)}
{min(list_months)}
''')

def get_total(list):
    total = 0
    for mean in list: total += mean
    return total
def get_average(total, list): return total / len(list)

if __name__ == '__main__': main()