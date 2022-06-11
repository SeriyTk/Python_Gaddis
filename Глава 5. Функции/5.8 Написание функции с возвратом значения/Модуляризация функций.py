def main():
    sales = get_sales()
    advanced_pay = get_advanced_pay()
    comm_rate = determine_comm_rate(sales)
    pay = sales * comm_rate - advanced_pay
    print(f'Выплата составляет ${pay:.2f}', sep=' ')
    if pay < 0: print('Продавец должен возместить разницу компании.')

def get_sales(): return float(input('Bвeдитe сумму месячных продаж: '))
def get_advanced_pay(): return float(input('Aвaнcoвaя вьmлата: '))
def determine_comm_rate(sales):
    if sales < 10000.00: rate = 0.10
    elif 10000 <= sales <= 14999.99: rate = 0.12
    elif 15000 <= sales <= 17999.99: rate = 0.14
    elif 18000 <= sales <= 21999.99: rate = 0.16
    else: rate = 0.18
    return rate


main()