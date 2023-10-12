ANNUAL_PROFIT = 0.23
def Sales_forecast():
    planned_amount = float(input('Введите плановую сумму общего объема продаж: '))
    profit = ANNUAL_PROFIT * planned_amount
    print(f'''Прибыль {profit:.2f}''')


if __name__ == '__main__': Sales_forecast = Sales_forecast()
