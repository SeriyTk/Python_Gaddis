def main():
    try:
        gross_pay =( int(input('Cкoлькo часов вы отработали? ')) *
                     float(input('Bвeдитe почасовую ставку:')))
        print(f'Зарплата: ${gross_pay:.2f}', sep='')
    except ValueError as err: print(err)


def main():
    total = 0
    try:
        for line in open('sales.txt'): total += float(line)
        print(f'{total:.2f}')
    except Exception as err: print(err)

main()
