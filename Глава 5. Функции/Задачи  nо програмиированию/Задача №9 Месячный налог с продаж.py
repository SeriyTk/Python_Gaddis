FEDERAL_TAX = 0.05
MUNICIPAL_TAX = 0.025


def main():
    tax(float(input('Общий объем продаж за месяц: ')))

def tax(par): print(f'''   
Сумма муниципального налога: {par * MUNICIPAL_TAX};
сумма федерального налога: {par * FEDERAL_TAX};
общий налог с продаж: {par * MUNICIPAL_TAX + par * FEDERAL_TAX}
''')


main()
