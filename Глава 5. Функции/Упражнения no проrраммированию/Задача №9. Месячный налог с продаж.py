FEDERAL_TAX = 0.05
MUNICIPAL_TAX = 0.025
def Monthly_tax():
    volume_sales = float(input('Общий объем продаж: '))
    sum_mun_tax = volume_sales * MUNICIPAL_TAX
    sum_fed_tax = volume_sales * FEDERAL_TAX
    total_tax = sum_fed_tax + sum_mun_tax
    print(f'''
Сумма муниципального налога с продаж: {sum_mun_tax};
сумма федерального налога с продаж: {sum_fed_tax};
 общий налог с продаж: {total_tax}
''')

if __name__ == '__main__': Monthly_tax()