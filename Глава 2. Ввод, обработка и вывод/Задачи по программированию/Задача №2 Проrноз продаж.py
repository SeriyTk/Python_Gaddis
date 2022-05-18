PROFIT = 0.23
def Sales_forecast():
    sales_volume = float(input('Плановая сумма общего объема продаж: '))
    future_profit = sales_volume * PROFIT
    print(f'Будущая прибыль {future_profit:,.2f}')


Sales_forecast()
