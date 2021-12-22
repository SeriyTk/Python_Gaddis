def Sales_forecast():
    ANNUAL_PROFIT = 0.23
    total_sales = float(input('Введите сумму: '))
    profit = total_sales * ANNUAL_PROFIT
    print(f'Прибыль составит {profit}.')


Sales_forecast()
