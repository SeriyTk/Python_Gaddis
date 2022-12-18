def Sales_forecast():
    PROF = 0.23
    planned_amount = float(input("Введите плановую сумму: "))
    profit = planned_amount * PROF
    print(f'Будет получена прибыль {profit:,.2f}')

Sales_forecast()