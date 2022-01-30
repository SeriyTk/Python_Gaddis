FED_TAX = 0.05
COUNCIL_TAX = 0.025


def Monthly_sales_tax():
    volume_of_sales = float(input('Общий объем продаж за месяц: '))
    sum_fed_tax = volume_of_sales * FED_TAX
    sum_council_tax = volume_of_sales * COUNCIL_TAX
    total_tax = sum_fed_tax + sum_council_tax
    print(f'Сумма федерального налога: {sum_fed_tax:,.2f}.')
    print(f'Сумма муниципального налога: {sum_council_tax:,.2f}.')
    print(f'Общий налог с продаж: {total_tax:,.2f}.')


Monthly_sales_tax()
