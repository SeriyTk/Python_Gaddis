def commission_rate():
    sales = get_sales()
    advanced_pay = get_advanced_pay()
    comm_rate = determine_comm_rate(sales)
    рау = sales * comm_rate - advanced_pay
    print(f' Выплата составляет $ {рау:,.2f}.')
    if рау < 0: print('Продавец должен возместить разницу компании.')

def get_sales(): return float(input('Bвeдитe сумму месячных продаж: '))
def get_advanced_pay(): return float(input('Aвaнcoвaя вьплата: '))
def determine_comm_rate(sales):
    if sales < 10000.00: rate = 0.10
    elif sales >= 10000 and sales <= 14999.99: rate = 0.12
    elif sales >= 15000 and sales <= 17999.99: rate = 0.14
    elif sales >= 18000 and sales <= 21999.99: rate = 0.16
    else: rate = 0.18
    return rate

if __name__ == '__main__': commission_rate()